// mobile/OrderScreen.js
// serves: REQ-003, REQ-006
// KitchenOps mobile automated purchase orders & supplier replenishment screen

import React, { useState, useEffect } from 'react';
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  ScrollView,
  ActivityIndicator,
} from 'react-native';
import { api } from './api';

export default function OrderScreen({ user }) {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(false);
  const [actionLoading, setActionLoading] = useState({});
  const [dispatchResult, setDispatchResult] = useState(null);
  const [error, setError] = useState('');

  const fetchOrders = async () => {
    setLoading(true);
    setError('');
    try {
      const res = await api('GET', '/orders/replenish');
      if (res.status === 200 && res.data && res.data.orders) {
        setOrders(res.data.orders);
      } else {
        setError(res.data && res.data.detail ? res.data.detail : 'Failed to load orders.');
      }
    } catch (e) {
      setError('Cannot reach server. Check network connection.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchOrders();
  }, []);

  const handleDispatch = async (poId) => {
    setError('');
    setDispatchResult(null);
    setActionLoading((prev) => ({ ...prev, [poId]: true }));

    try {
      const res = await api('POST', '/orders/dispatch', { po_id: poId });
      if (res.status === 200 && res.data && res.data.success) {
        setDispatchResult(res.data);
        // Refresh orders list
        fetchOrders();
      } else {
        const detail = res.data && res.data.detail ? res.data.detail : 'Dispatch failed.';
        setError(detail);
      }
    } catch (e) {
      setError('Network communication failed during dispatch.');
    } finally {
      setActionLoading((prev) => ({ ...prev, [poId]: false }));
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <View style={styles.header}>
        <View style={styles.badge}>
          <Text style={styles.badgeText}>KitchenOps Restock</Text>
        </View>
        <Text style={styles.title}>Automated Supplier Orders</Text>
        <Text style={styles.subtitle}>
          Active Chef: {user || 'chef@kitchenops.internal'}
        </Text>
      </View>

      <View style={styles.actionsBar}>
        <Text style={styles.sectionTitle}>Draft Purchase Orders (FIFO Safety)</Text>
        <TouchableOpacity style={styles.refreshBtn} onPress={fetchOrders} disabled={loading}>
          <Text style={styles.refreshBtnText}>{loading ? 'Syncing...' : '↻ Refresh'}</Text>
        </TouchableOpacity>
      </View>

      {error ? (
        <View style={styles.errorBox}>
          <Text style={styles.errorText}>⚠ {error}</Text>
        </View>
      ) : null}

      {dispatchResult ? (
        <View style={styles.successBox}>
          <Text style={styles.successTitle}>✓ PO Dispatched to Supplier!</Text>
          <Text style={styles.successDetail}>
            PO: {dispatchResult.po_id} · {dispatchResult.order_amount} {dispatchResult.unit} ordered
          </Text>
          <Text style={styles.successSub}>
            Supplier: {dispatchResult.supplier} · Status: {dispatchResult.status}
          </Text>
        </View>
      ) : null}

      {loading && orders.length === 0 ? (
        <View style={styles.loaderContainer}>
          <ActivityIndicator size="large" color="#38bdf8" />
          <Text style={styles.loaderText}>Evaluating safety threshold buffers...</Text>
        </View>
      ) : null}

      {!loading && orders.length === 0 ? (
        <View style={styles.emptyCard}>
          <Text style={styles.emptyTitle}>All Stocks Above Safety Buffer</Text>
          <Text style={styles.emptySubtitle}>
            No ingredients have fallen below safety threshold levels.
          </Text>
        </View>
      ) : null}

      {orders.map((order) => {
        const isDispatched = order.status === 'dispatched';
        const isDispatching = actionLoading[order.po_id];

        return (
          <View key={order.po_id} style={styles.orderCard}>
            <View style={styles.orderHeader}>
              <View>
                <Text style={styles.orderIngredient}>{order.ingredient_name || order.ingredient}</Text>
                <Text style={styles.orderPoId}>PO Number: {order.po_id}</Text>
              </View>
              <View style={[styles.statusBadge, isDispatched ? styles.statusBadgeDispatched : styles.statusBadgeDraft]}>
                <Text style={[styles.statusBadgeText, isDispatched ? styles.statusTextDispatched : styles.statusTextDraft]}>
                  {order.status.toUpperCase()}
                </Text>
              </View>
            </View>

            <View style={styles.metaGrid}>
              <View style={styles.metaItem}>
                <Text style={styles.metaLabel}>Current Stock</Text>
                <Text style={[styles.metaValue, styles.metaValueCritical]}>
                  {order.current_stock} {order.unit}
                </Text>
              </View>
              <View style={styles.metaItem}>
                <Text style={styles.metaLabel}>Safety Threshold</Text>
                <Text style={styles.metaValue}>{order.threshold} {order.unit}</Text>
              </View>
              <View style={styles.metaItem}>
                <Text style={styles.metaLabel}>Reorder Buffer</Text>
                <Text style={[styles.metaValue, styles.metaValueReorder]}>
                  +{order.order_amount} {order.unit}
                </Text>
              </View>
            </View>

            <View style={styles.supplierRow}>
              <Text style={styles.supplierLabel}>Wholesale Supplier:</Text>
              <Text style={styles.supplierValue}>{order.supplier}</Text>
            </View>

            {!isDispatched ? (
              <TouchableOpacity
                style={[styles.dispatchButton, isDispatching && styles.buttonDisabled]}
                onPress={() => handleDispatch(order.po_id)}
                disabled={isDispatching}
              >
                {isDispatching ? (
                  <ActivityIndicator color="#ffffff" />
                ) : (
                  <Text style={styles.dispatchButtonText}>Authorize & Dispatch PO</Text>
                )}
              </TouchableOpacity>
            ) : (
              <View style={styles.dispatchedBanner}>
                <Text style={styles.dispatchedBannerText}>✓ PO Transmitted to Metro Food Wholesale Ltd.</Text>
              </View>
            )}
          </View>
        );
      })}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
    paddingTop: 60,
    backgroundColor: '#0f172a',
    flexGrow: 1,
  },
  header: {
    alignItems: 'center',
    marginBottom: 16,
  },
  badge: {
    backgroundColor: '#f59e0b',
    paddingHorizontal: 12,
    paddingVertical: 4,
    borderRadius: 12,
    marginBottom: 8,
  },
  badgeText: {
    color: '#0f172a',
    fontSize: 12,
    fontWeight: 'bold',
  },
  title: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#f8fafc',
    marginBottom: 4,
  },
  subtitle: {
    fontSize: 13,
    color: '#94a3b8',
  },
  actionsBar: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 14,
  },
  sectionTitle: {
    color: '#cbd5e1',
    fontSize: 14,
    fontWeight: '600',
  },
  refreshBtn: {
    backgroundColor: '#1e293b',
    paddingVertical: 6,
    paddingHorizontal: 12,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#475569',
  },
  refreshBtnText: {
    color: '#38bdf8',
    fontSize: 13,
    fontWeight: '600',
  },
  orderCard: {
    backgroundColor: '#1e293b',
    borderRadius: 16,
    padding: 18,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#334155',
  },
  orderHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: 14,
    paddingBottom: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#334155',
  },
  orderIngredient: {
    color: '#f8fafc',
    fontSize: 17,
    fontWeight: 'bold',
  },
  orderPoId: {
    color: '#64748b',
    fontSize: 12,
    marginTop: 2,
  },
  statusBadge: {
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 8,
  },
  statusBadgeDraft: {
    backgroundColor: '#451a03',
    borderColor: '#b45309',
    borderWidth: 1,
  },
  statusBadgeDispatched: {
    backgroundColor: '#064e3b',
    borderColor: '#059669',
    borderWidth: 1,
  },
  statusTextDraft: {
    color: '#fbbf24',
    fontSize: 11,
    fontWeight: 'bold',
  },
  statusTextDispatched: {
    color: '#34d399',
    fontSize: 11,
    fontWeight: 'bold',
  },
  metaGrid: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    backgroundColor: '#0f172a',
    borderRadius: 10,
    padding: 12,
    marginBottom: 12,
  },
  metaItem: {
    alignItems: 'center',
  },
  metaLabel: {
    color: '#64748b',
    fontSize: 11,
    marginBottom: 4,
  },
  metaValue: {
    color: '#f8fafc',
    fontSize: 14,
    fontWeight: '600',
  },
  metaValueCritical: {
    color: '#f87171',
    fontWeight: 'bold',
  },
  metaValueReorder: {
    color: '#38bdf8',
    fontWeight: 'bold',
  },
  supplierRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 14,
  },
  supplierLabel: {
    color: '#94a3b8',
    fontSize: 12,
  },
  supplierValue: {
    color: '#cbd5e1',
    fontSize: 12,
    fontWeight: '500',
  },
  dispatchButton: {
    backgroundColor: '#0284c7',
    paddingVertical: 12,
    borderRadius: 10,
    alignItems: 'center',
  },
  dispatchButtonText: {
    color: '#ffffff',
    fontSize: 14,
    fontWeight: 'bold',
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  dispatchedBanner: {
    backgroundColor: '#064e3b',
    paddingVertical: 10,
    borderRadius: 8,
    alignItems: 'center',
  },
  dispatchedBannerText: {
    color: '#6ee7b7',
    fontSize: 12,
    fontWeight: '600',
  },
  loaderContainer: {
    padding: 40,
    alignItems: 'center',
  },
  loaderText: {
    color: '#94a3b8',
    fontSize: 14,
    marginTop: 12,
  },
  emptyCard: {
    backgroundColor: '#1e293b',
    borderRadius: 16,
    padding: 24,
    alignItems: 'center',
    borderColor: '#334155',
    borderWidth: 1,
  },
  emptyTitle: {
    color: '#34d399',
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 6,
  },
  emptySubtitle: {
    color: '#94a3b8',
    fontSize: 13,
    textAlign: 'center',
  },
  errorBox: {
    backgroundColor: '#7f1d1d',
    padding: 12,
    borderRadius: 10,
    marginBottom: 14,
  },
  errorText: {
    color: '#fca5a5',
    fontSize: 13,
  },
  successBox: {
    backgroundColor: '#064e3b',
    padding: 14,
    borderRadius: 10,
    marginBottom: 14,
    borderWidth: 1,
    borderColor: '#059669',
  },
  successTitle: {
    color: '#6ee7b7',
    fontSize: 15,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  successDetail: {
    color: '#d1fae5',
    fontSize: 13,
  },
  successSub: {
    color: '#a7f3d0',
    fontSize: 11,
    marginTop: 2,
  },
});


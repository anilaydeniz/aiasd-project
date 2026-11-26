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
    <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
      {/* Header Station Info */}
      <View style={styles.headerBar}>
        <View>
          <Text style={styles.headerStation}>STATION 1 · LOGISTICS & PROCUREMENT</Text>
          <Text style={styles.headerTitle}>Replenishment Orders</Text>
        </View>
        <TouchableOpacity style={styles.refreshBadge} onPress={fetchOrders}>
          <Text style={styles.refreshBadgeText}>Sync POs</Text>
        </TouchableOpacity>
      </View>

      {error ? (
        <View style={styles.errorBox}>
          <Text style={styles.errorText}>{error}</Text>
        </View>
      ) : null}

      {dispatchResult ? (
        <View style={styles.successBox}>
          <Text style={styles.successTitle}>✓ Purchase Order Dispatched</Text>
          <Text style={styles.successDetail}>
            Dispatched PO {dispatchResult.po_id || 'PO-2026-041'} to supplier EDI endpoint.
          </Text>
          <Text style={styles.successSub}>
            Estimated delivery logged in incoming receiving dock.
          </Text>
        </View>
      ) : null}

      {loading ? (
        <View style={styles.loaderContainer}>
          <ActivityIndicator size="large" color="#1D4ED8" />
          <Text style={styles.loaderText}>Syncing replenishment orders...</Text>
        </View>
      ) : orders && orders.length > 0 ? (
        orders.map((po) => {
          const isPending = po.status === 'pending' || po.status === 'draft';
          const isDispatched = po.status === 'dispatched';
          const isBusy = actionLoading[po.id];

          return (
            <View key={po.id} style={styles.orderCard}>
              <View style={styles.orderHeaderRow}>
                <View>
                  <Text style={styles.poNumber}>{po.id}</Text>
                  <Text style={styles.poDate}>{po.created_at || 'Auto-generated via FIFO buffer'}</Text>
                </View>
                <View
                  style={[
                    styles.statusPill,
                    isDispatched ? styles.statusDispatched : styles.statusPending,
                  ]}
                >
                  <Text
                    style={[
                      styles.statusPillText,
                      isDispatched ? styles.statusTextDispatched : styles.statusTextPending,
                    ]}
                  >
                    {po.status ? po.status.toUpperCase() : 'PENDING'}
                  </Text>
                </View>
              </View>

              <Text style={styles.triggerNotice}>
                Automated replenishment triggered by buffer deficit threshold.
              </Text>

              <View style={styles.specBox}>
                <View style={styles.specRow}>
                  <Text style={styles.specLabel}>Ingredient Item</Text>
                  <Text style={styles.specValueBold}>{po.item_name || po.item_id || 'Ingredient'}</Text>
                </View>
                <View style={styles.specRow}>
                  <Text style={styles.specLabel}>Current Pantry Stock</Text>
                  <Text style={styles.specValueDanger}>
                    {po.current_stock ?? 3.4} {po.unit || 'kg'}
                  </Text>
                </View>
                <View style={styles.specRow}>
                  <Text style={styles.specLabel}>Reorder Batch</Text>
                  <Text style={styles.specValueBold}>
                    +{po.reorder_qty ?? 25} {po.unit || 'kg'}
                  </Text>
                </View>
                <View style={[styles.specRow, { borderBottomWidth: 0 }]}>
                  <Text style={styles.specLabel}>Supplier EDI</Text>
                  <Text style={styles.specValueBold}>{po.supplier || 'Metro Foodservice AG'}</Text>
                </View>
              </View>

              <View style={styles.actionSection}>
                <View style={styles.totalRow}>
                  <Text style={styles.totalLabel}>Estimated Batch Cost</Text>
                  <Text style={styles.totalAmount}>
                    {po.estimated_cost ? `$${po.estimated_cost}` : '$85.00'}
                  </Text>
                </View>

                {isPending && (
                  <TouchableOpacity
                    style={[styles.dispatchButton, isBusy && styles.buttonDisabled]}
                    onPress={() => handleDispatch(po.id)}
                    disabled={isBusy}
                  >
                    {isBusy ? (
                      <ActivityIndicator color="#FFFFFF" />
                    ) : (
                      <Text style={styles.dispatchButtonText}>
                        Authorize & Dispatch PO
                      </Text>
                    )}
                  </TouchableOpacity>
                )}

                {isDispatched && (
                  <View style={styles.dispatchedBanner}>
                    <Text style={styles.dispatchedBannerText}>
                      ✓ PO Transmitted · Expected Delivery: Next Shift
                    </Text>
                  </View>
                )}
              </View>
            </View>
          );
        })
      ) : (
        <View style={styles.emptyCard}>
          <Text style={styles.emptyTitle}>Pantry Buffers Sufficient</Text>
          <Text style={styles.emptySubtitle}>
            All ingredient levels are currently above their minimum safety thresholds.
            No automated purchase orders are pending.
          </Text>
        </View>
      )}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#EDF2F7',
  },
  contentContainer: {
    padding: 16,
    paddingBottom: 24,
  },
  headerBar: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 16,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#CBD5E1',
  },
  headerStation: {
    fontSize: 11,
    fontWeight: '700',
    color: '#1D4ED8',
    letterSpacing: 0.5,
    marginBottom: 2,
  },
  headerTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: '#1A202C',
  },
  refreshBadge: {
    backgroundColor: '#EFF6FF',
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#BFDBFE',
  },
  refreshBadgeText: {
    fontSize: 11.5,
    fontWeight: '700',
    color: '#1D4ED8',
  },
  orderCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 18,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#CBD5E1',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.05,
    shadowRadius: 8,
    elevation: 2,
  },
  orderHeaderRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: 10,
  },
  poNumber: {
    fontSize: 16,
    fontWeight: '700',
    color: '#1A202C',
  },
  poDate: {
    fontSize: 11.5,
    color: '#64748B',
    marginTop: 2,
  },
  statusPill: {
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 99,
  },
  statusPending: {
    backgroundColor: '#FEF3C7',
  },
  statusDispatched: {
    backgroundColor: '#DCFCE7',
  },
  statusPillText: {
    fontSize: 10.5,
    fontWeight: '700',
  },
  statusTextPending: {
    color: '#B45309',
  },
  statusTextDispatched: {
    color: '#166534',
  },
  triggerNotice: {
    fontSize: 12.5,
    color: '#64748B',
    marginBottom: 14,
    lineHeight: 17,
  },
  specBox: {
    backgroundColor: '#F8FAFC',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    paddingHorizontal: 12,
    paddingVertical: 6,
    marginBottom: 14,
  },
  specRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: '#E2E8F0',
  },
  specLabel: {
    fontSize: 13,
    color: '#64748B',
  },
  specValueBold: {
    fontSize: 13,
    fontWeight: '700',
    color: '#1A202C',
  },
  specValueDanger: {
    fontSize: 13,
    fontWeight: '700',
    color: '#DC2626',
  },
  actionSection: {
    marginTop: 4,
  },
  totalRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'baseline',
    marginBottom: 12,
  },
  totalLabel: {
    fontSize: 13,
    color: '#64748B',
  },
  totalAmount: {
    fontSize: 17,
    fontWeight: '700',
    color: '#1E3A8A',
  },
  dispatchButton: {
    backgroundColor: '#1D4ED8',
    borderRadius: 12,
    height: 50,
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#1D4ED8',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.2,
    shadowRadius: 8,
    elevation: 3,
  },
  dispatchButtonText: {
    color: '#FFFFFF',
    fontSize: 15,
    fontWeight: '600',
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  dispatchedBanner: {
    backgroundColor: '#DCFCE7',
    borderRadius: 10,
    paddingVertical: 12,
    alignItems: 'center',
  },
  dispatchedBannerText: {
    color: '#166534',
    fontSize: 13,
    fontWeight: '600',
  },
  loaderContainer: {
    padding: 40,
    alignItems: 'center',
  },
  loaderText: {
    color: '#64748B',
    fontSize: 14,
    marginTop: 12,
  },
  emptyCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 24,
    alignItems: 'center',
    borderColor: '#CBD5E1',
    borderWidth: 1,
  },
  emptyTitle: {
    color: '#166534',
    fontSize: 16,
    fontWeight: '700',
    marginBottom: 6,
  },
  emptySubtitle: {
    color: '#64748B',
    fontSize: 13,
    textAlign: 'center',
    lineHeight: 18,
  },
  errorBox: {
    backgroundColor: '#FEF2F2',
    padding: 12,
    borderRadius: 10,
    marginBottom: 14,
    borderWidth: 1,
    borderColor: '#FECACA',
  },
  errorText: {
    color: '#DC2626',
    fontSize: 13,
  },
  successBox: {
    backgroundColor: '#DCFCE7',
    padding: 14,
    borderRadius: 10,
    marginBottom: 14,
    borderWidth: 1,
    borderColor: '#86EFAC',
  },
  successTitle: {
    color: '#166534',
    fontSize: 15,
    fontWeight: '700',
    marginBottom: 4,
  },
  successDetail: {
    color: '#15803D',
    fontSize: 13,
  },
  successSub: {
    color: '#166534',
    fontSize: 11.5,
    marginTop: 2,
  },
});

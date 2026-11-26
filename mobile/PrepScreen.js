// mobile/PrepScreen.js
// serves: REQ-002, REQ-006
// KitchenOps mobile kitchen prep screen: portion preparation, automated BOM stock deduction & buffer alerts

import React, { useState, useEffect } from 'react';
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  ScrollView,
  ActivityIndicator,
  Alert,
} from 'react-native';
import { api } from './api';

export default function PrepScreen({ user, onLogout }) {
  const [recipeId, setRecipeId] = useState('rigatoni_pomodoro');
  const [portions, setPortions] = useState(10);
  const [inventory, setInventory] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const fetchInventory = async () => {
    try {
      const res = await api('GET', '/inventory/levels');
      if (res.status === 200 && res.data && res.data.items) {
        setInventory(res.data.items);
      }
    } catch (e) {
      // Non-blocking
    }
  };

  useEffect(() => {
    fetchInventory();
  }, []);

  const handleAdjustPortions = (delta) => {
    setPortions((prev) => Math.max(1, prev + delta));
  };

  const handlePrep = async () => {
    setError('');
    setResult(null);
    if (!portions || portions <= 0) {
      setError('Please select at least 1 portion to prepare.');
      return;
    }

    setLoading(true);
    try {
      const res = await api('POST', '/prep/portions', {
        recipe_id: recipeId,
        portions: portions,
      });

      if (res.status === 200 && res.data && res.data.success) {
        setResult(res.data);
        fetchInventory();
      } else {
        const detail =
          res.data && res.data.detail ? res.data.detail : 'Preparation request failed.';
        setError(typeof detail === 'string' ? detail : 'Preparation error.');
      }
    } catch (e) {
      setError('Network communication error with KitchenOps server.');
    } finally {
      setLoading(false);
    }
  };

  // Recipe specs
  const recipeName = 'Rigatoni Pomodoro';
  const recipeStation = 'Hot Line 1';

  // Projected ingredient depletion calculation
  const pastaDepletion = (portions * 0.12).toFixed(2);
  const tomatoDepletion = (portions * 0.08).toFixed(2);
  const oliveOilDepletion = (portions * 0.015).toFixed(3);

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
      {/* Header Station Info */}
      <View style={styles.headerBar}>
        <View>
          <Text style={styles.headerStation}>STATION 1 · PREP & COOKING</Text>
          <Text style={styles.headerTitle}>{recipeName}</Text>
        </View>
        <View style={styles.stationBadge}>
          <Text style={styles.stationBadgeText}>{recipeStation}</Text>
        </View>
      </View>

      {/* Main Preparation Control Card */}
      <View style={styles.card}>
        <Text style={styles.sectionTitle}>Portion Configuration</Text>
        <Text style={styles.sectionSubtitle}>
          Adjust batch quantity to calculate automated bill-of-materials stock deduction.
        </Text>

        <View style={styles.stepperContainer}>
          <TouchableOpacity
            style={styles.stepButton}
            onPress={() => handleAdjustPortions(-5)}
          >
            <Text style={styles.stepButtonText}>-5</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.stepButton}
            onPress={() => handleAdjustPortions(-1)}
          >
            <Text style={styles.stepButtonText}>-1</Text>
          </TouchableOpacity>

          <View style={styles.portionDisplay}>
            <Text style={styles.portionNumber}>{portions}</Text>
            <Text style={styles.portionUnit}>PORTIONS</Text>
          </View>

          <TouchableOpacity
            style={styles.stepButton}
            onPress={() => handleAdjustPortions(1)}
          >
            <Text style={styles.stepButtonText}>+1</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.stepButton}
            onPress={() => handleAdjustPortions(5)}
          >
            <Text style={styles.stepButtonText}>+5</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.chipRow}>
          {[5, 10, 20, 50].map((count) => (
            <TouchableOpacity
              key={count}
              style={[
                styles.quickChip,
                portions === count && styles.quickChipActive,
              ]}
              onPress={() => setPortions(count)}
            >
              <Text
                style={[
                  styles.quickChipText,
                  portions === count && styles.quickChipTextActive,
                ]}
              >
                {count} pax
              </Text>
            </TouchableOpacity>
          ))}
        </View>

        {/* Projected BOM Depletion Box */}
        <View style={styles.depletionBox}>
          <Text style={styles.depletionTitle}>PROJECTED PANTRY DEPLETION</Text>
          <View style={styles.depletionRow}>
            <Text style={styles.depletionItem}>Rigatoni Pasta</Text>
            <Text style={styles.depletionQty}>-{pastaDepletion} kg</Text>
          </View>
          <View style={styles.depletionRow}>
            <Text style={styles.depletionItem}>San Marzano Tomatoes</Text>
            <Text style={styles.depletionQty}>-{tomatoDepletion} kg</Text>
          </View>
          <View style={[styles.depletionRow, { borderBottomWidth: 0 }]}>
            <Text style={styles.depletionItem}>Extra Virgin Olive Oil</Text>
            <Text style={styles.depletionQty}>-{oliveOilDepletion} L</Text>
          </View>
        </View>

        {error ? (
          <View style={styles.errorBox}>
            <Text style={styles.errorText}>{error}</Text>
          </View>
        ) : null}

        {result ? (
          <View style={styles.successBox}>
            <Text style={styles.successTitle}>✓ Preparation Batch Recorded</Text>
            <Text style={styles.successDetail}>
              Successfully prepared {result.portions_prepared || portions} portions.
            </Text>
            <Text style={styles.successSub}>
              Pantry stock decremented via FIFO batch rules.
            </Text>
          </View>
        ) : null}

        <TouchableOpacity
          style={[styles.primaryButton, loading && styles.buttonDisabled]}
          onPress={handlePrep}
          disabled={loading}
        >
          {loading ? (
            <ActivityIndicator color="#FFFFFF" />
          ) : (
            <Text style={styles.primaryButtonText}>
              Confirm Preparation & Deplete Stock
            </Text>
          )}
        </TouchableOpacity>
      </View>

      {/* Live Pantry Stock Card with Buffer Alerts */}
      <View style={styles.card}>
        <View style={styles.cardHeaderRow}>
          <Text style={styles.sectionTitle}>Live Pantry Stock</Text>
          <TouchableOpacity onPress={fetchInventory}>
            <Text style={styles.refreshLink}>Refresh</Text>
          </TouchableOpacity>
        </View>
        <Text style={styles.sectionSubtitle}>
          Real-time ingredient levels synced across all kitchen terminals.
        </Text>

        {inventory ? (
          <View style={styles.inventoryList}>
            {Object.entries(inventory).map(([itemKey, itemData]) => {
              const currentStock = itemData.current ?? itemData.qty ?? 0;
              const unit = itemData.unit || 'kg';
              const buffer = itemData.buffer_threshold || itemData.threshold || 5;
              const isLow = currentStock <= buffer;

              return (
                <View key={itemKey} style={styles.inventoryRow}>
                  <View style={styles.inventoryInfo}>
                    <Text style={styles.inventoryName}>
                      {itemData.name || itemKey.replace(/_/g, ' ')}
                    </Text>
                    <Text style={styles.inventoryMeta}>
                      Buffer Threshold: {buffer} {unit}
                    </Text>
                  </View>
                  <View style={styles.inventoryRight}>
                    <Text
                      style={[
                        styles.inventoryAmount,
                        isLow && styles.inventoryAmountLow,
                      ]}
                    >
                      {currentStock} {unit}
                    </Text>
                    {isLow && (
                      <View style={styles.bufferBadge}>
                        <Text style={styles.bufferBadgeText}>⚠ BUFFER ALERT</Text>
                      </View>
                    )}
                  </View>
                </View>
              );
            })}
          </View>
        ) : (
          <ActivityIndicator color="#1D4ED8" style={{ marginVertical: 20 }} />
        )}
      </View>
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
  stationBadge: {
    backgroundColor: '#DCFCE7',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 99,
  },
  stationBadgeText: {
    fontSize: 11.5,
    fontWeight: '700',
    color: '#166534',
  },
  card: {
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
  cardHeaderRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  refreshLink: {
    fontSize: 12.5,
    color: '#1D4ED8',
    fontWeight: '600',
  },
  sectionTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: '#1A202C',
    marginBottom: 4,
  },
  sectionSubtitle: {
    fontSize: 12.5,
    color: '#64748B',
    marginBottom: 16,
    lineHeight: 17,
  },
  stepperContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#F8FAFC',
    borderRadius: 14,
    padding: 10,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    marginBottom: 14,
  },
  stepButton: {
    backgroundColor: '#E2E8F0',
    width: 44,
    height: 44,
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
    marginHorizontal: 4,
  },
  stepButtonText: {
    fontSize: 15,
    fontWeight: '700',
    color: '#1E293B',
  },
  portionDisplay: {
    alignItems: 'center',
    paddingHorizontal: 20,
    minWidth: 110,
  },
  portionNumber: {
    fontSize: 32,
    fontWeight: '800',
    color: '#1E3A8A',
  },
  portionUnit: {
    fontSize: 10,
    fontWeight: '700',
    color: '#64748B',
    letterSpacing: 1,
  },
  chipRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 16,
  },
  quickChip: {
    flex: 1,
    backgroundColor: '#F1F5F9',
    borderRadius: 10,
    paddingVertical: 8,
    alignItems: 'center',
    marginHorizontal: 3,
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  quickChipActive: {
    backgroundColor: '#DBEAFE',
    borderColor: '#93C5FD',
  },
  quickChipText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#475569',
  },
  quickChipTextActive: {
    color: '#1D4ED8',
    fontWeight: '700',
  },
  depletionBox: {
    backgroundColor: '#F8FAFC',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 12,
    marginBottom: 16,
  },
  depletionTitle: {
    fontSize: 11,
    fontWeight: '700',
    color: '#64748B',
    letterSpacing: 0.5,
    marginBottom: 8,
  },
  depletionRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 6,
    borderBottomWidth: 1,
    borderBottomColor: '#E2E8F0',
  },
  depletionItem: {
    fontSize: 13,
    color: '#1E293B',
  },
  depletionQty: {
    fontSize: 13,
    fontWeight: '700',
    color: '#DC2626',
  },
  primaryButton: {
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
  primaryButtonText: {
    color: '#FFFFFF',
    fontSize: 15,
    fontWeight: '600',
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  errorBox: {
    backgroundColor: '#FEF2F2',
    borderWidth: 1,
    borderColor: '#FECACA',
    borderRadius: 10,
    padding: 12,
    marginBottom: 14,
  },
  errorText: {
    color: '#DC2626',
    fontSize: 13,
  },
  successBox: {
    backgroundColor: '#DCFCE7',
    borderWidth: 1,
    borderColor: '#86EFAC',
    borderRadius: 10,
    padding: 12,
    marginBottom: 14,
  },
  successTitle: {
    color: '#166534',
    fontSize: 14,
    fontWeight: '700',
    marginBottom: 2,
  },
  successDetail: {
    color: '#15803D',
    fontSize: 12.5,
  },
  successSub: {
    color: '#166534',
    fontSize: 11.5,
    marginTop: 2,
  },
  inventoryList: {
    marginTop: 4,
  },
  inventoryRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#F1F5F9',
  },
  inventoryInfo: {
    flex: 1,
  },
  inventoryName: {
    fontSize: 14,
    fontWeight: '600',
    color: '#1E293B',
    textTransform: 'capitalize',
  },
  inventoryMeta: {
    fontSize: 11.5,
    color: '#64748B',
    marginTop: 2,
  },
  inventoryRight: {
    alignItems: 'flex-end',
  },
  inventoryAmount: {
    fontSize: 15,
    fontWeight: '700',
    color: '#1E293B',
  },
  inventoryAmountLow: {
    color: '#DC2626',
  },
  bufferBadge: {
    backgroundColor: '#FEF2F2',
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 6,
    marginTop: 3,
    borderWidth: 1,
    borderColor: '#FECACA',
  },
  bufferBadgeText: {
    fontSize: 9.5,
    fontWeight: '700',
    color: '#DC2626',
  },
});

// mobile/PrepScreen.js
// serves: REQ-002, REQ-006
// KitchenOps mobile kitchen prep screen: portion preparation & stock depletion

import React, { useState, useEffect } from 'react';
import {
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity,
  ScrollView,
  ActivityIndicator,
} from 'react-native';
import { api } from './api';

export default function PrepScreen({ user, onLogout }) {
  const [recipeId, setRecipeId] = useState('rigatoni_pomodoro');
  const [portions, setPortions] = useState('10');
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

  const handlePrep = async () => {
    setError('');
    setResult(null);
    const numPortions = parseInt(portions, 10);
    if (!numPortions || numPortions <= 0) {
      setError('Please enter a valid portion count greater than 0.');
      return;
    }

    setLoading(true);
    try {
      const res = await api('POST', '/prep/portions', {
        recipe_id: recipeId,
        portions: numPortions,
      });

      if (res.status === 200 && res.data && res.data.success) {
        setResult(res.data);
        fetchInventory();
      } else {
        const detail = res.data && res.data.detail ? res.data.detail : 'Preparation failed.';
        setError(detail);
      }
    } catch (e) {
      setError('Network communication failed.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <View style={styles.header}>
        <View style={styles.badge}>
          <Text style={styles.badgeText}>KitchenOps Mobile</Text>
        </View>
        <Text style={styles.title}>Dish Prep & FIFO Stock</Text>
        <Text style={styles.subtitle}>
          Logged in: {user || 'chef@kitchenops.internal'}
        </Text>
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Selected Recipe</Text>
        <View style={styles.recipeBox}>
          <Text style={styles.recipeName}>Rigatoni Pomodoro</Text>
          <Text style={styles.recipeMeta}>
            Bill of Materials: 120g pasta, 80g tomato sauce per portion
          </Text>
        </View>

        <Text style={styles.label}>Portions to Prepare</Text>
        <TextInput
          style={styles.input}
          keyboardType="numeric"
          value={portions}
          onChangeText={setPortions}
          placeholder="e.g. 10"
          placeholderTextColor="#64748b"
        />

        {error ? (
          <View style={styles.errorBox}>
            <Text style={styles.errorText}>⚠ {error}</Text>
          </View>
        ) : null}

        {result ? (
          <View style={styles.successBox}>
            <Text style={styles.successTitle}>✓ Prep Logged Successfully!</Text>
            <Text style={styles.successDetail}>
              Portions: {result.portions} · Audit ID: {result.audit_log_id}
            </Text>
            {result.depleted && result.depleted.map((item, idx) => (
              <Text key={idx} style={styles.depletedItem}>
                - Depleted {item.ingredient}: {item.amount_kg} kg
              </Text>
            ))}
          </View>
        ) : null}

        <TouchableOpacity
          style={[styles.button, loading && styles.buttonDisabled]}
          onPress={handlePrep}
          disabled={loading}
        >
          {loading ? (
            <ActivityIndicator color="#ffffff" />
          ) : (
            <Text style={styles.buttonText}>Log Portions & Deduct Stock</Text>
          )}
        </TouchableOpacity>
      </View>

      {inventory ? (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Live Inventory Stock Levels</Text>
          {Object.entries(inventory).map(([ing, qty]) => (
            <View key={ing} style={styles.stockRow}>
              <Text style={styles.stockLabel}>{ing}</Text>
              <Text style={styles.stockValue}>{qty} kg</Text>
            </View>
          ))}
        </View>
      ) : null}

      {onLogout ? (
        <TouchableOpacity style={styles.logoutButton} onPress={onLogout}>
          <Text style={styles.logoutText}>Log Out</Text>
        </TouchableOpacity>
      ) : null}
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
    marginBottom: 20,
  },
  badge: {
    backgroundColor: '#0284c7',
    paddingHorizontal: 12,
    paddingVertical: 4,
    borderRadius: 12,
    marginBottom: 8,
  },
  badgeText: {
    color: '#ffffff',
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
  card: {
    backgroundColor: '#1e293b',
    borderRadius: 16,
    padding: 20,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#334155',
  },
  cardTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#f8fafc',
    marginBottom: 12,
  },
  recipeBox: {
    backgroundColor: '#0f172a',
    padding: 12,
    borderRadius: 8,
    marginBottom: 16,
  },
  recipeName: {
    color: '#38bdf8',
    fontSize: 16,
    fontWeight: '600',
  },
  recipeMeta: {
    color: '#64748b',
    fontSize: 12,
    marginTop: 4,
  },
  label: {
    color: '#cbd5e1',
    fontSize: 14,
    marginBottom: 6,
    fontWeight: '500',
  },
  input: {
    backgroundColor: '#0f172a',
    borderWidth: 1,
    borderColor: '#475569',
    borderRadius: 10,
    padding: 12,
    color: '#ffffff',
    fontSize: 16,
    marginBottom: 14,
  },
  button: {
    backgroundColor: '#2563eb',
    paddingVertical: 14,
    borderRadius: 10,
    alignItems: 'center',
    marginTop: 8,
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  buttonText: {
    color: '#ffffff',
    fontSize: 15,
    fontWeight: 'bold',
  },
  errorBox: {
    backgroundColor: '#7f1d1d',
    padding: 10,
    borderRadius: 8,
    marginBottom: 12,
  },
  errorText: {
    color: '#fca5a5',
    fontSize: 13,
  },
  successBox: {
    backgroundColor: '#064e3b',
    padding: 12,
    borderRadius: 8,
    marginBottom: 14,
  },
  successTitle: {
    color: '#6ee7b7',
    fontWeight: 'bold',
    fontSize: 14,
    marginBottom: 4,
  },
  successDetail: {
    color: '#a7f3d0',
    fontSize: 12,
    marginBottom: 4,
  },
  depletedItem: {
    color: '#d1fae5',
    fontSize: 12,
  },
  stockRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: '#334155',
  },
  stockLabel: {
    color: '#94a3b8',
    fontSize: 14,
    textTransform: 'capitalize',
  },
  stockValue: {
    color: '#f8fafc',
    fontSize: 14,
    fontWeight: '600',
  },
  logoutButton: {
    alignItems: 'center',
    padding: 16,
    marginTop: 8,
  },
  logoutText: {
    color: '#ef4444',
    fontSize: 14,
    fontWeight: '600',
  },
});

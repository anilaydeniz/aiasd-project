// mobile/LoginScreen.js
// serves: REQ-001, REQ-006
import React, { useState } from 'react';
import {
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
  ActivityIndicator,
  SafeAreaView,
} from 'react-native';
import { api, setToken } from './api';

export default function LoginScreen({ onLoginSuccess }) {
  const [step, setStep] = useState(1); // 1: enter email, 2: enter 4-digit code, 3: logged in
  const [email, setEmail] = useState('');
  const [code, setCode] = useState('');
  const [userProfile, setUserProfile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [isError, setIsError] = useState(false);

  // Step 1: Request 4-digit verification code sent to email
  const handleRequestCode = async () => {
    if (!email || !email.includes('@')) {
      setMessage('Please enter a valid email address');
      setIsError(true);
      return;
    }

    setLoading(true);
    setMessage('');
    setIsError(false);

    const res = await api('POST', '/auth/code', { email: email.trim().toLowerCase() });
    setLoading(false);

    if (res.status === 200) {
      setStep(2);
      setMessage('A 4-digit verification code has been sent to your email.');
      setIsError(false);
    } else {
      const err = res.data && res.data.detail ? res.data.detail : 'Failed to request login code';
      setMessage(typeof err === 'string' ? err : 'Validation error');
      setIsError(true);
    }
  };

  // Step 2: Verify code and obtain authentication token
  const handleVerifyCode = async () => {
    if (!code || code.trim().length !== 4) {
      setMessage('Please enter the 4-digit code');
      setIsError(true);
      return;
    }

    setLoading(true);
    setMessage('');
    setIsError(false);

    const res = await api('POST', '/auth/token', {
      email: email.trim().toLowerCase(),
      code: code.trim(),
    });

    if (res.status === 200 && res.data && res.data.token) {
      setToken(res.data.token);
      // Fetch authenticated user profile via GET /auth/me
      const meRes = await api('GET', '/auth/me');
      setLoading(false);

      if (meRes.status === 200) {
        setUserProfile(meRes.data);
        setStep(3);
        setMessage('');
        if (onLoginSuccess) {
          onLoginSuccess(meRes.data, res.data.token);
        }
      } else {
        setMessage('Could not verify profile from server');
        setIsError(true);
      }
    } else {
      setLoading(false);
      const err = res.data && res.data.detail ? res.data.detail : 'Wrong code. Check email and try again.';
      setMessage(typeof err === 'string' ? err : 'Invalid code');
      setIsError(true);
    }
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <View style={styles.card}>
        <View style={styles.header}>
          <Text style={styles.badge}>KitchenOps Mobile</Text>
          <Text style={styles.title}>Chef Authentication</Text>
          <Text style={styles.description}>
            Passwordless OTP login for commercial kitchen stations
          </Text>
        </View>

        {step === 1 && (
          <View style={styles.form}>
            <Text style={styles.label}>Kitchen Email Address</Text>
            <TextInput
              style={styles.input}
              placeholder="chef@kitchenops.internal"
              placeholderTextColor="#64748b"
              autoCapitalize="none"
              keyboardType="email-address"
              value={email}
              onChangeText={setEmail}
            />
            <TouchableOpacity
              style={styles.button}
              onPress={handleRequestCode}
              disabled={loading}
            >
              {loading ? (
                <ActivityIndicator color="#ffffff" />
              ) : (
                <Text style={styles.buttonText}>Send 4-Digit Code</Text>
              )}
            </TouchableOpacity>
          </View>
        )}

        {step === 2 && (
          <View style={styles.form}>
            <Text style={styles.label}>4-Digit Verification Code</Text>
            <TextInput
              style={[styles.input, styles.codeInput]}
              placeholder="1234"
              placeholderTextColor="#64748b"
              keyboardType="number-pad"
              maxLength={4}
              value={code}
              onChangeText={setCode}
            />
            <TouchableOpacity
              style={styles.button}
              onPress={handleVerifyCode}
              disabled={loading}
            >
              {loading ? (
                <ActivityIndicator color="#ffffff" />
              ) : (
                <Text style={styles.buttonText}>Verify & Log In</Text>
              )}
            </TouchableOpacity>
            <TouchableOpacity
              style={styles.linkButton}
              onPress={() => {
                setStep(1);
                setMessage('');
                setIsError(false);
              }}
            >
              <Text style={styles.linkText}>← Change email address</Text>
            </TouchableOpacity>
          </View>
        )}

        {step === 3 && userProfile && (
          <View style={styles.successBox}>
            <Text style={styles.successTitle}>Active Session Verified</Text>
            <Text style={styles.sessionLabel}>Logged in user:</Text>
            <Text style={styles.userEmail}>
              {userProfile.user || userProfile.email || email}
            </Text>
            <View style={styles.statusPill}>
              <Text style={styles.statusPillText}>Online · Kitchen Staff</Text>
            </View>
          </View>
        )}

        {message ? (
          <View style={[styles.alert, isError ? styles.alertError : styles.alertSuccess]}>
            <Text style={[styles.alertText, isError ? styles.alertTextError : styles.alertTextSuccess]}>
              {message}
            </Text>
          </View>
        ) : null}
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#0f172a',
    justifyContent: 'center',
    padding: 16,
  },
  card: {
    backgroundColor: '#1e293b',
    borderRadius: 16,
    padding: 24,
    borderWidth: 1,
    borderColor: '#334155',
  },
  header: {
    alignItems: 'center',
    marginBottom: 24,
  },
  badge: {
    backgroundColor: '#0ea5e9',
    color: '#ffffff',
    fontSize: 12,
    fontWeight: 'bold',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
    marginBottom: 8,
    overflow: 'hidden',
  },
  title: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#f8fafc',
    marginBottom: 6,
  },
  description: {
    fontSize: 13,
    color: '#94a3b8',
    textAlign: 'center',
  },
  form: {
    width: '100%',
  },
  label: {
    fontSize: 14,
    fontWeight: '600',
    color: '#cbd5e1',
    marginBottom: 8,
  },
  input: {
    backgroundColor: '#0f172a',
    borderWidth: 1,
    borderColor: '#475569',
    borderRadius: 8,
    color: '#f8fafc',
    paddingHorizontal: 14,
    paddingVertical: 12,
    fontSize: 16,
    marginBottom: 16,
  },
  codeInput: {
    letterSpacing: 8,
    textAlign: 'center',
    fontSize: 24,
    fontWeight: 'bold',
  },
  button: {
    backgroundColor: '#0ea5e9',
    borderRadius: 8,
    paddingVertical: 14,
    alignItems: 'center',
    marginTop: 4,
  },
  buttonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  linkButton: {
    marginTop: 14,
    alignItems: 'center',
  },
  linkText: {
    color: '#38bdf8',
    fontSize: 14,
  },
  successBox: {
    backgroundColor: '#022c22',
    borderWidth: 1,
    borderColor: '#059669',
    borderRadius: 12,
    padding: 18,
    alignItems: 'center',
    marginTop: 8,
  },
  successTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#34d399',
    marginBottom: 10,
  },
  sessionLabel: {
    fontSize: 13,
    color: '#a7f3d0',
  },
  userEmail: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#ffffff',
    marginVertical: 4,
  },
  statusPill: {
    backgroundColor: '#065f46',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 20,
    marginTop: 8,
  },
  statusPillText: {
    color: '#6ee7b7',
    fontSize: 12,
    fontWeight: '600',
  },
  alert: {
    marginTop: 16,
    padding: 12,
    borderRadius: 8,
  },
  alertError: {
    backgroundColor: '#450a0a',
    borderColor: '#dc2626',
    borderWidth: 1,
  },
  alertSuccess: {
    backgroundColor: '#064e3b',
    borderColor: '#059669',
    borderWidth: 1,
  },
  alertText: {
    fontSize: 13,
    textAlign: 'center',
  },
  alertTextError: {
    color: '#fca5a5',
  },
  alertTextSuccess: {
    color: '#6ee7b7',
  },
});

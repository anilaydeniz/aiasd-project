// mobile/App.js
import React, { useState } from 'react';
import { StyleSheet, View } from 'react-native';
import LoginScreen from './LoginScreen';

export default function App() {
  const [session, setSession] = useState(null);

  return (
    <View style={styles.container}>
      <LoginScreen onLoginSuccess={(user, token) => setSession({ user, token })} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0f172a',
  },
});

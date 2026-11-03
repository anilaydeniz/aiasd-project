// mobile/App.js
// KitchenOps main mobile container with authentication flow & prep screen

import React, { useState } from 'react';
import { StyleSheet, View } from 'react-native';
import LoginScreen from './LoginScreen';
import PrepScreen from './PrepScreen';

export default function App() {
  const [session, setSession] = useState(null);

  return (
    <View style={styles.container}>
      {!session ? (
        <LoginScreen
          onLoginSuccess={(user, token) => setSession({ user, token })}
        />
      ) : (
        <PrepScreen
          user={session.user}
          onLogout={() => setSession(null)}
        />
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0f172a',
  },
});

# Week 7 — AI log

## The change I asked for

I gave the assistant mobile/PrepScreen.js and asked for one single change based on my classmate tester feedback: when an ingredient stock level is below 5.0 kg, display a safety buffer alert badge next to the ingredient name so the kitchen staff is warned before stock hits zero.

## The change I received

The assistant returned a diff that modified mobile/PrepScreen.js. It added the stockLabelContainer wrapper and the conditional warning badge with **<Text style={styles.lowStockWarningText}>⚠ Buffer Alert</Text>** when qty is less than 5.0 kg. It also added the corresponding styling rules in styles. However, the assistant also tried to alter the layout alignment of the entire container and suggested changing default portion input values.

## What I refused, and why

I refused the suggested layout alignment restructuring and the change to default portion input values. I only wanted the buffer alert badge to inform the chef about low stock levels without modifying the existing portion prep calculation or the container dimensions. I kept only the conditional badge and its styling definitions, and discarded the extra layout adjustments.

## The commit, and the phone

I committed the accepted change in commit d67eab3 with the message "week07: resolve tester feedback with low stock alert and record round 2 mobile runs". On my iPhone 13 running iOS 18 in Expo Go, I opened the Kitchen Prep screen: Cooking Cream at 3.5 kg clearly displayed the red ⚠ Buffer Alert badge, while ingredients above 5.0 kg showed normal values, confirming that the change works as expected.

## Evidence — the exchange and the diff

```text
ME:
In mobile/PrepScreen.js, when an ingredient stock level in Live Inventory Stock Levels is below 5.0 kg, show a buffer alert badge next to the ingredient name. Do not change anything else.

AI:
I will add the low stock warning badge to mobile/PrepScreen.js. Here is the updated stock row:
<Text style={styles.lowStockWarningText}>⚠ Buffer Alert</Text>

TERMINAL:
diff --git a/mobile/PrepScreen.js b/mobile/PrepScreen.js
index 8a4816e..3660cbf 100644
--- a/mobile/PrepScreen.js
+++ b/mobile/PrepScreen.js
@@ -158,8 +158,15 @@ export default function PrepScreen({ user, onLogout }) {
           <Text style={styles.cardTitle}>Live Inventory Stock Levels</Text>
           {Object.entries(inventory).map(([ing, qty]) => (
             <View key={ing} style={styles.stockRow}>
-              <Text style={styles.stockLabel}>{ing}</Text>
-              <Text style={styles.stockValue}>{qty} kg</Text>
+              <View style={styles.stockLabelContainer}>
+                <Text style={styles.stockLabel}>{ing}</Text>
+                {qty < 5.0 ? (
+                  <View style={styles.lowStockWarningBadge}>
+                    <Text style={styles.lowStockWarningText}>⚠ Buffer Alert</Text>
+                  </View>
+                ) : null}
+              </View>
+              <Text style={[styles.stockValue, qty < 5.0 && styles.stockValueLow]}>{qty} kg</Text>
             </View>
           ))}
         </View>
@@ -327,10 +334,33 @@ const styles = StyleSheet.create({
   stockRow: {
     flexDirection: 'row',
     justifyContent: 'space-between',
+    alignItems: 'center',
     paddingVertical: 8,
     borderBottomWidth: 1,
     borderBottomColor: '#334155',
   },
+  stockLabelContainer: {
+    flexDirection: 'row',
+    alignItems: 'center',
+  },
+  lowStockWarningBadge: {
+    backgroundColor: '#7f1d1d',
+    borderColor: '#ef4444',
+    borderWidth: 1,
+    paddingHorizontal: 6,
+    paddingVertical: 2,
+    borderRadius: 6,
+    marginLeft: 8,
+  },
+  lowStockWarningText: {
+    color: '#fca5a5',
+    fontSize: 10,
+    fontWeight: 'bold',
+  },
+  stockValueLow: {
+    color: '#f87171',
+    fontWeight: 'bold',
+  },
   stockLabel: {
     color: '#94a3b8',
     fontSize: 14,
```

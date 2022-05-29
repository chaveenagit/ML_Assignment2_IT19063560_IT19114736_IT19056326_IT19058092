import * as React from 'react';
import {Button, View, LogBox} from 'react-native';
import {createDrawerNavigator} from '@react-navigation/drawer';
import { NavigationContainer } from '@react-navigation/native';
import HomeScreen from './screens/HomeScreen';
import NotificationsScreen from './screens/NotificationsScreen';

const Drawer = createDrawerNavigator();
LogBox.ignoreLogs(['Warnings: ...']);
LogBox.ignoreAllLogs();

export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator initialRouteName="Home">
        <Drawer.Screen name="Home" component={HomeScreen} />
        <Drawer.Screen name="Results" component={NotificationsScreen} />
      </Drawer.Navigator>
    </NavigationContainer>
  );
}
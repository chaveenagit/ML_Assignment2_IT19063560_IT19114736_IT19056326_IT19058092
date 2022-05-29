import React, {useState} from 'react';
import {
  StyleSheet,
  View,
  TouchableOpacity,
  Dimensions
} from 'react-native';
import { useDimensions, useDeviceOrientation } from '@react-native-community/hooks'
import Icon from 'react-native-vector-icons/Ionicons';
import RNFetchBlob from 'rn-fetch-blob';
import storage from '@react-native-firebase/storage';
import { utils } from '@react-native-firebase/app';

export default Header = ({navigation,upload}) => {
    // RNFetchBlob.fs.ls(RNFetchBlob.fs.dirs.SDCardDir+'/Pictures/RNSketchCanvas/').then(async(files) => {
    //   const reference = storage().ref('/image.png');
    //   await reference.putFile((RNFetchBlob.fs.dirs.SDCardDir+'/Pictures/RNSketchCanvas/'+files[0]).toString());

    // })
    // .then( () => {
    //   console.log('successfully')
    // })
    // .catch(error => console.log(error))
 
    return(
        <View style={{
          height: 60, 
          padding: 15, 
          justifyContent: "space-between",
          backgroundColor: 'darkslateblue', 
          width: useDimensions().screen.width,
          flexDirection: 'row'}}>
          <TouchableOpacity onPress={() => {navigation.toggleDrawer()}}><Icon name="menu-outline" size={30} color="white" /></TouchableOpacity>
          <TouchableOpacity onPress={() => {upload()}}><Icon name="refresh" size={30} color="white" /></TouchableOpacity>
        </View>
    );
}

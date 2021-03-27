import { StatusBar } from 'expo-status-bar';
import React from 'react';
import {Image, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import madGoldenLord from './assets/MadAndGolden.jpg';

export default function App() {
 
  let openImagePickerAsync = async () => {
    let permissionResult = await ImagePicker.requestMediaLibraryPermissionsAsync();
    
    if (permissionResult.granted === false) {
      alert("Permission to access camera roll is required!");
      return;
    }

    let pickerResult = await ImagePicker.launchImageLibraryAsync();
    console.log(pickerResult);
  
  }
  


 
  return (
    <View style={styles.container}>
      <Image source={madGoldenLord} style= {styles.madGoldenLord} />
      <Text style={{color: '#888', fontSize: 18}}>
        To share a photo from your phone with a friend, just press the button below!
      </Text>
      
      <TouchableOpacity onPress={openImagePickerAsync}style={ styles.button}>
          <Text style={styles.buttonText}>Pick a photo</Text>
      </TouchableOpacity>
      
    </View>

  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  madGoldenLord: {
    width: 310,
    height: 450,
    marginBottom: 10,
  },
  button: {
    backgroundColor: 'blue',
    padding: 20,
    borderRadius: 5,
  },
  buttonText: {
    fontSize: 20,
    color: '#fff',
  },  
});

import * as React from 'react';
// import  {useState, useEffect} from 'react';
import { SectionList, StyleSheet, View, Text, Button } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { BarCodeScanner } from 'expo-barcode-scanner';

const navigation = createStackNavigator();
const Stack = createStackNavigator();
const styles = StyleSheet.create({
  homeStyle: {
    flex: 1,
    alignItems: 'center',
  },
  dataStyle: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center'
  },
  sectionHeader: {
    paddingTop: 2,
    paddingLeft: 10,
    paddingRight: 10,
    paddingBottom: 2,
    fontSize: 14,
    fontWeight: 'bold',
    backgroundColor: 'rgba(247,247,247,1.0)',
  },
  item: {
    padding: 10,
    fontSize: 18,
    height: 44,
  }
});


function HomeScreen( {navigation} ){
  const [hasPermission, sethasPermission] = React.useState(null);
  const [scanned, setScanned] = React.useState(false);

  React.useEffect(() => {
    (async () => {
      const { status } = await BarCodeScanner.requestPermissionsAsync();
      sethasPermission(status === 'granted');
    })();
  }, []);

  const handleBarCodeScanned = ({type, data}) => {
    setScanned(true);
    var upc = data as String;
    alert(`Bar code type ${type} and data ${upc}`);
  };

  if (hasPermission === null) {
    return <Text>Requesting for camera permission</Text>;
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  return (
    <View style={styles.homeStyle}>
      <Text>Home Screen</Text>
        <BarCodeScanner 
          onBarCodeScanned={scanned ? undefined : handleBarCodeScanned}
          style={StyleSheet.absoluteFillObject}
        />
      {scanned && <Button title={'Go to results'} onPress={() => navigation.navigate('Details')}/>}
    </View>
  );
};

function DetailsScreen({navigation}) {
  return(
    <View style={styles.dataStyle}>
      <Text>Details Screen</Text>
      <Button
        title="Go to Home"
        onPress={() => navigation.navigate('Home')}
      />
      <SectionList sections={[
        {title: 'ht', data: ['3.79']},
        {title: 'walmart', data: ['2.98']},
        {title: 'amazon-fresh', data: ['3.00']},
        {title: 'stop-share', data: ['3.00']},
        {title: 'bj', data: ['Price not found']},
        {title: 'heb', data: ['Price not found']},
        {title: 'class', data: ['UPCA']},
        {title: 'code', data: ['020685000294']},
        {title: 'company', data: ['Cape Cod']},
        {title: 'description', data: ['Cape cod Original 40% reduced fat kettle cooked potato chips']},
      ]}
        renderItem={({item}) => <Text style={styles.item}>{item}</Text>}
        renderSectionHeader={({section}) => <Text style={styles.sectionHeader}>{section.title}</Text>}
        keyExtractor={(item, index)=>index}
      />
    </View>
  );
};
/*
{"ht": 3.79, "walmart": 2.98, "amazon-fresh": 3.0, "stop-shop": 3.0, "bj": "Price not found", "heb": "Price not found"}
|{"class": "UPCA", "code": "020685000294", "company": "Cape Cod", "description": "Cape cod Original 40% redced fat kettle cooked potato chips", uced fat kettle cooked potato chips", "image_url": "https://images-na.ssl-images-amazon.com/images/I/81VdkBdj1XL._SL1500_.jpg", "size": "", "status": "active"}
*/
function App() {

  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}


export default App;
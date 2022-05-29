import React, {useState} from 'react';
import {
  View,
  Text,
  FlatList
} from 'react-native';
import Header from '../components/Header';

export default function NotificationsScreen({ navigation, upload }) {
    const [sss, setSss] = useState([1,3,2,43,11,12,123,13,45,66,88,99,33,344343,3443434232,233232,2323]);
    return (
        <View style={{flex:1}}>
            <Header navigation={navigation} upload={ () => {}}/>
            <View style={{flex: 1}}>
                <FlatList 
                    data={sss}
                    keyExtractor={ (s) => s}
                    renderItem={(s) => {
                        return(
                            <Text onPress={() => alert(2)}>dffdf</Text>
                        );
                    }}
                />
            </View>
        </View>
    );
}


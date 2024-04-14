import React, { useEffect, useState } from 'react';
import { Button, View, Text, ActivityIndicator } from 'react-native';
import API, { endpoints } from '../configs/API';

const HomeScreen = ({ navigation }) => {
  const [nhanvien, setnhanvien] = useState(null);

  useEffect(() => {
    const loadNhanVien = async() => {
        try{
            let res = await API.get(endpoints['nhanvien']);
            setnhanvien(res.data.results)
        } catch(ex){
            console.error(ex);
        }
    }
    loadNhanVien();
  }, []);

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
      <Button
        title="Go to Details"
        onPress={() => navigation.navigate('Details')}
      />
      {nhanvien===null?<ActivityIndicator/>:<>
        {nhanvien.map(c => (
            <View key={c.id}>
                <Text>{c.Ten_NV}</Text>
            </View>
        ))}
      </>}
    </View>
  );
}

export default HomeScreen

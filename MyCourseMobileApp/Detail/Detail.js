import React from 'react';
import { Button, View, Text, ViewBase } from 'react-native';

export default function DetailsScreen({navigation}) {
    return (
      <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
        <Text>Details Screen</Text>
        <Button
          title='Go To Home'
          onPress={() => navigation.navigate('Home')}
        />
      </View>
    );
  }
import React, {useState} from 'react';
import {Text, StyleSheet} from 'react-native';
import {SafeAreaView, SafeAreaProvider} from 'react-native-safe-area-context';

const TextInANest = () => {
  const [titleText, setTitleText] = useState("System");
  const bodyText = 'Hi! Im Jem and I would like to share with you all about my experience on our sysarc subject so we start by talking about which subject that we would make. And I suggest the enrollment system because I know some of the teachers in my old school, and thought about it because I really thought it was easy but in reality its not its really hard as heck. But we really did finish it and defended it. Im happy about that though. And yeah thats all i can think because usually I do all the coding and help my fellow groups about our system and we really did a great job doing it so yeah. For the other parts that I did I kinda am a busy doing it in the sysarc so I had to do my main job as an game developer I usually need to write 20 to 30k words a months because i have rent to pay and that is really suck but atleast im doing my dream job while studying so yeah. Im happy about that and I think that is all i can share since some of the other part of my jobs are really private and some of my boss really dont want to share me some of the information about our game and also my team. I dont want them to share any parts of my game because this is really private. So yeah even i have a lot of job to do I still finishes all my work in sysarc';

  const onPressTitle = () => {
    setTitleText("Bird's Nest [pressed]");
  };

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.container}>
        <Text style={styles.baseText}>
          <Text style={styles.titleText} onPress={onPressTitle}>
            {titleText}
            {'\n'}
            {'\n'}
          </Text>
          <Text numberOfLines={5}>{bodyText}</Text>
        </Text>
      </SafeAreaView>
    </SafeAreaProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  baseText: {
    fontFamily: 'Cochin',
  },
  titleText: {
    fontSize: 20,
    fontWeight: 'bold',
  },
});

export default TextInANest;
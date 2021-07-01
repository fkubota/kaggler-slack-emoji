<template>
    <v-app>
    <v-app-bar color="#208ea3" dark app class='title'>
      <v-toolbar-title justify='center'>kaggler-slack-emoji</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
              <v-btn icon href='https://twitter.com/fkubota_' v-bind="attrs" v-on="on">
                  <v-icon>mdi-twitter</v-icon>
              </v-btn>
          </template>
          <span>twitter</span>
      </v-tooltip>
      <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
              <v-btn icon href='https://github.com/fkubota' v-bind="attrs" v-on="on">
                  <v-icon>mdi-github</v-icon>
              </v-btn>
          </template>
          <span>GitHub</span>
      </v-tooltip>
      <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
              <v-btn icon href='https://github.com/fkubota/kaggler-slack-emoji' v-bind="attrs" v-on="on">
                  <v-icon>mdi-code-tags</v-icon>
              </v-btn>
          </template>
          <span>Source Code</span>
      </v-tooltip>
    </v-app-bar>
    <v-content class='mt-5'>
        <v-container>
            <v-row justify="center">
              <v-img src='./../../emoji/kaggle/cv.png' max-height="50" max-width="50" contain ></v-img>
              <v-img src='./../../emoji/kaggle/cv.png' max-height="50" max-width="50" contain ></v-img>

								<!-- <ul>                                                                       -->
        <!--           <li>{{images}}</li>                                              -->
								<!-- </ul>                                                                      -->

            </v-row>
        </v-container>
    </v-content>
    </v-app>
</template>

<script>
  export default {
      name: 'App',
      components: {
        },
		};
</script>

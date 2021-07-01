import os
import re
from glob import glob

list_path_kaggle = sorted(glob('./../../emoji/kaggle/*'))
list_path_zatsudan = sorted(glob('./../../emoji/zatsudan/*'))
oa = "{ on, attrs }"


################
# kaggle emoji #
################
s_text = ''
for path in list_path_kaggle:
    tool_tip = os.path.basename(path).split('.')[0]
    base_text = f'<v-tooltip bottom> <template v-slot:activator="{oa}"> <v-img src="{path}" max-height="50" max-width="50" contain v-bind="attrs" v-on="on"> </v-img> </template> <span>{tool_tip}</span> </v-tooltip>'
    s_text = s_text + base_text

path = 'home2.vue'
with open(path) as f:
    text = f.read()

pattern = r'<v-row justify="left">(.+?)</v-row>'
matched_list = re.findall(pattern, text)
text_new = text.replace(matched_list[0], s_text)

with open(path, mode='w') as f:
        f.write(text_new)


##################
# zatsudan emoji #
##################
s_text = ''
for path in list_path_zatsudan:
    tool_tip = os.path.basename(path).split('.')[0]
    base_text = f'<v-tooltip bottom> <template v-slot:activator="{oa}"> <v-img src="{path}" max-height="50" max-width="50" contain v-bind="attrs" v-on="on"> </v-img> </template> <span>{tool_tip}</span> </v-tooltip>'
    s_text = s_text + base_text

path = 'home2.vue'
with open(path) as f:
    text = f.read()

pattern = r'<v-row  justify="left">(.+?)</v-row>'
matched_list = re.findall(pattern, text)
text_new = text.replace(matched_list[0], s_text)

with open(path, mode='w') as f:
        f.write(text_new)

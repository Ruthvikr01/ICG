from  package import *

# create mapping of image to captions
mapping = {}
with open('captions_doc.txt', 'r') as file:
    captions_doc = file.read()
element = tqdm(captions_doc.split('\n'))
for line in element: 
    tokens = line.split(',')
    
    if len(line) < 2:
        continue
    image_id, caption = tokens[0], tokens[1:] # remove extension from image ID # convert caption list to string
    image_id = image_id.split('.')[0]
    caption = " ".join(caption)
    # create list if needed
    if image_id not in mapping: 
        mapping[image_id] = []
    #store the caption
    mapping[image_id].append(caption)

print(len(mapping))

all_captions = []
for key in mapping:
    for caption in mapping[key]:
        all_captions.append(caption)

print(len(all_captions))        

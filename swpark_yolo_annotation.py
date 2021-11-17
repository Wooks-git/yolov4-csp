from glob import glob
import json
import os

a = glob('/home/ubuntu/swpark/darknet/build/darknet/x64/data/obj/*.jpg')
print(len(a))

a = glob('/home/ubuntu/swpark/darknet/build/darknet/x64/data/obj/*.txt')
print(len(a))
# path = '/home/ubuntu/swpark/data/valid/con_without_hand/'
# label_path = glob(path + '*.json')

# save_dir = '/home/ubuntu/swpark/darknet/build/darknet/x64/data/obj/'
# # print(len(glob(save_dir+'*.jpg')))

# for i in label_path:
#     with open(i, 'r', encoding='utf-8') as f:
        
#         data = json.load(f)
#         width = data['FileInfo']['Width']
#         height = data['FileInfo']['Height']
#         file_name = data['FileInfo']['FileName'].split('.')[0]

#         face_coord = 'empty'
#         phone_coord = 'empty'
#         cigar_coord = 'empty'

#         try:
#             if data['ObjectInfo']['BoundingBox']['Face']['isVisible']:
#                 face_coord = data['ObjectInfo']['BoundingBox']['Face']['Position']

#             else:
#                 face_coord = 'empty'

#         except KeyError:
#             pass

#         try:
#             if data['ObjectInfo']['BoundingBox']['Phone']['isVisible']:
#                 phone_coord = data['ObjectInfo']['BoundingBox']['Phone']['Position']

#             else:
#                 phone_coord = 'empty'
#         except KeyError:
#             pass

#         try:
#             if data['ObjectInfo']['BoundingBox']['Cigar']['isVisible']:
#                 cigar_coord = data['ObjectInfo']['BoundingBox']['Cigar']['Position']

#             else:
#                 cigar_coord = 'empty'
#         except KeyError:
#             pass

#     with open(save_dir + file_name + '.txt', 'w', encoding= ' utf-8') as ff:
#         if type(face_coord[0]) == int:
#             dw = 1./width
#             dh = 1./height
#             x = (face_coord[0] + face_coord[2])/2.0 - 1
#             y = (face_coord[1] + face_coord[3])/2.0 - 1
#             w = face_coord[2] - face_coord[0]
#             h = face_coord[3] - face_coord[1]
#             x = x*dw
#             w = w*dw
#             y = y*dh
#             h = h*dh

#             ff.write('0 {} {} {} {}\n'.format(x,y,w,h))
#         else:
#             pass
        
#         if type(phone_coord[0]) == int:
#             dw = 1./width
#             dh = 1./height
#             x = (phone_coord[0] + phone_coord[2])/2.0 - 1
#             y = (phone_coord[1] + phone_coord[3])/2.0 - 1
#             w = phone_coord[2] - phone_coord[0]
#             h = phone_coord[3] - phone_coord[1]
#             x = x*dw
#             w = w*dw
#             y = y*dh
#             h = h*dh

#             ff.write('1 {} {} {} {}\n'.format(x,y,w,h))

#         else:
#             pass

#         if type(cigar_coord[0]) == int:
#             dw = 1./width
#             dh = 1./height
#             x = (cigar_coord[0] + cigar_coord[2])/2.0 - 1
#             y = (cigar_coord[1] + cigar_coord[3])/2.0 - 1
#             w = cigar_coord[2] - cigar_coord[0]
#             h = cigar_coord[3] - cigar_coord[1]
#             x = x*dw
#             w = w*dw
#             y = y*dh
#             h = h*dh

#             ff.write('2 {} {} {} {}\n'.format(x,y,w,h))

#         else:
#             pass
    
#     print(save_dir + file_name + ' create!!!@')
        
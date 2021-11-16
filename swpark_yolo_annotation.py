from glob import glob
import json
import os

path = '/home/ubuntu/swpark/data/valid/'
save_dir = '/home/ubuntu/swpark/darknet/build/darknet/x64/data/obj/'
# print(len(glob(save_dir+'*.jpg')))

label_path = glob(path + 'con_without_hand/*.json')

for i in label_path:
    with open(i, 'r', encoding='utf-8') as f:
        data = json.load(f)
        width = data['FileInfo']['Width']
        height = data['FileInfo']['Height']
        file_name = data['FileInfo']['FileName'].split('.')[0]

        try:
            if data['ObjectInfo']['BoundingBox']['Face']['isVisible']:
                face_coord = data['ObjectInfo']['BoundingBox']['Face']['Position']
        except KeyError:
            pass

        try:
            if data['ObjectInfo']['BoundingBox']['Phone']['isVisible']:
                phone_coord = data['ObjectInfo']['BoundingBox']['Phone']['Position']
        except KeyError:
            pass

        try:
            if data['ObjectInfo']['BoundingBox']['Cigar']['isVisible']:
                cigar_coord = data['ObjectInfo']['BoundingBox']['Cigar']['Position']
        except KeyError:
            pass

    with open(save_dir + file_name + '.txt', 'w', encoding= ' utf-8') as ff:
        try:
            if type(face_coord[0]) == int:
                dw = 1./width
                dh = 1./height
                x = (face_coord[0] + face_coord[2])/2.0 - 1
                y = (face_coord[1] + face_coord[3])/2.0 - 1
                w = face_coord[2] - face_coord[0]
                h = face_coord[3] - face_coord[1]
                x = x*dw
                w = w*dw
                y = y*dh
                h = h*dh

                ff.write(f'0 {x} {y} {w} {h}\n')

        except NameError:
            pass
        
        try:
            if type(phone_coord[0]) == int:
                dw = 1./width
                dh = 1./height
                x = (phone_coord[0] + phone_coord[2])/2.0 - 1
                y = (phone_coord[1] + phone_coord[3])/2.0 - 1
                w = phone_coord[2] - phone_coord[0]
                h = phone_coord[3] - phone_coord[1]
                x = x*dw
                w = w*dw
                y = y*dh
                h = h*dh

                ff.write(f'1 {x} {y} {w} {h}\n')
        except NameError:
            pass

        try:
            if type(cigar_coord[0]) == int:
                dw = 1./width
                dh = 1./height
                x = (cigar_coord[0] + cigar_coord[2])/2.0 - 1
                y = (cigar_coord[1] + cigar_coord[3])/2.0 - 1
                w = cigar_coord[2] - cigar_coord[0]
                h = cigar_coord[3] - cigar_coord[1]
                x = x*dw
                w = w*dw
                y = y*dh
                h = h*dh

                ff.write(f'2 {x} {y} {w} {h}\n')
        except NameError:
            pass
    
    print(save_dir + file_name + ' create!!!')
        
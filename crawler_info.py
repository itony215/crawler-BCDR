for num in range(1, 1011):
    url = "http://bcdr.inegi.up.pt/patient/" + str(num)
    res = requests.get(url, cookies={'bcdr': 'carq66jbvf6an5cl4bhhqbut55'})
    soup = BeautifulSoup(res.text, 'html.parser')
    tag_name = 'div#segmentation_image a'
    if soup.select(tag_name):
        articles = soup.select(tag_name)
        image = 'http://bcdr.inegi.up.pt' + articles[0]['href']
    else:
        continue
        #print(image,num)
    tabletag = soup.select('table#lesions td')
    values = ','.join(str(v) for v in tabletag[1:2])
    if "Right" in values:
        breast_laterality = "right"
    else:
        breast_laterality = "left"

    t1 = soup.select('input#mammography_nodule')
    t2 = soup.select('input#mammography_microcalcification')
    t3 = soup.select('input#mammography_calcification')
    t4 = soup.select('input#mammography_axillary_adenopathy')
    t5 = soup.select('input#mammography_architectural_distortion')
    t6 = soup.select('input#mammography_stroma_distortion')
    v1 = ','.join(str(v) for v in t1)
    if "checked" in v1:
        asymmetry_type = "nodule"
    v2 = ','.join(str(v) for v in t2)
    if "checked" in v2:
        asymmetry_type = "microcalcification"
    v3 = ','.join(str(v) for v in t3)
    if "checked" in v3:
        asymmetry_type = "calcification"
    v4 = ','.join(str(v) for v in t4)
    if "checked" in v4:
        asymmetry_type = "axillary_adenopathy"
    v5 = ','.join(str(v) for v in t5)
    if "checked" in v5:
        asymmetry_type = "architectural_distortion"
    v6 = ','.join(str(v) for v in t6)
    if "checked" in v6:
        asymmetry_type = "stroma_distortion"

    b = soup.select('table.table_show td')
    b = ",".join(str(v) for v in b[2:3])
    if "BIRADS 1" in b:
        BIARDS_category = "BIRADS 1"
    if "BIRADS 2" in b:
        BIARDS_category = "BIRADS 2"
    if "BIRADS 3" in b:
        BIARDS_category = "BIRADS 3"
    if "BIRADS 4" in b:
        BIARDS_category = "BIRADS 4"
    if "BIRADS 5" in b:
        BIARDS_category = "BIRADS 5"
    if "BIRADS 6" in b:
        BIARDS_category = "BIRADS 6"

    s1 = soup.select('table.segmentation_field td')
    s1 = ",".join(str(v) for v in s1[19:20])
    st = re.sub(r'[<td></td>]+', '', s1)  # 用正则表达式消去输入中的字母
    shape = st
    import json

    test_dict = {'id': num, 'breast_laterality': breast_laterality, 'asymmetry_type': asymmetry_type,
                 'BIARDS_category': BIARDS_category, 'shape': shape, 'image_url': image, 'source': 'BCDR'}
    #print(test_dict)
    #print(type(test_dict))
    #dumps 将数据转换成字符串
    json_str = json.dumps(test_dict)
    print(json_str + ",\n")
    #print(type(json_str))
    with open('./record.json', "a") as json_file:
        json_file.write("{},\n".format(json.dumps(json_str)))

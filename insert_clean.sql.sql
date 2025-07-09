INSERT INTO products (
    kaspi_code, name_cn, category_1, category_2, category_3, brand,
    description, image_paths,
    material_pendant, length_cm, type, color_metal, color_insert, gender,
    assay, material, insert_material, country, weight_grams, vendor_code, price_yuan
) VALUES (
    'AZIMA-Parago-00034', 'Swan手镯黑色天鹅项链', 'Украшения', 'Бижутерия', 'Колье', 'AZIMA',
    'Элегантное колье в форме чёрного лебедя. Идеально для особых случаев и подарков 🖤',
    ARRAY['images/00034_img1.png', 'images/00034_img2.jpg'],
    'Ювелирный сплав', '45', 'Колье', 'Чёрный', 'Нет', 'Для женщин',
    'Нет', 'Сплав', 'Нет', 'Китай', '12', 'Azima.Naz00034', 15.90
);

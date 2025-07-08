=# CREATE DATABASE azima_store;
CREATE DATABASE

=# \c azima_store
You are now connected to database "azima_store" as user "DB_USER".

azima_store=# CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    kaspi_code VARCHAR(20),
    name_cn TEXT,
    category_1 VARCHAR(50),
    category_2 VARCHAR(50),
    category_3 VARCHAR(50),
    brand VARCHAR(50),
    description TEXT,
    image_paths TEXT[],
    material_pendant VARCHAR(100),
    length_cm VARCHAR(10),
    type VARCHAR(50),
    color_metal VARCHAR(50),
    color_insert VARCHAR(50),
    gender VARCHAR(30),
    assay VARCHAR(30),
    material VARCHAR(50),
    insert_material VARCHAR(50),
    country VARCHAR(50),
    weight_grams VARCHAR(20),
    vendor_code VARCHAR(50),
    price_yuan NUMERIC(10, 2)
);
CREATE TABLE

azima_store=# INSERT INTO products (
    kaspi_code, name_cn, category_1, category_2, category_3, brand,
    description, image_paths,
    material_pendant, length_cm, type, color_metal, color_insert, gender,
    assay, material, insert_material, country, weight_grams, vendor_code, price_yuan
) VALUES (
    'AZIMA-Parago-00034', 'Swan手镯黑色天鹅项链', 'Украшения', 'Бижутерия', 'Колье', 'AZIMA',
    'Элегантное колье в форме чёрного лебедя. Идеально для особых случаев и подарков.',
    ARRAY['images/00034_img1.png', 'images/00034_img2.jpg'],
    'Ювелирный сплав', '45', 'Колье', 'Чёрный', 'Нет', 'Для женщин',
    'Нет', 'Сплав', 'Нет', 'Китай', '12', 'Azima.Naz00034', 15.90
);
INSERT 0 1


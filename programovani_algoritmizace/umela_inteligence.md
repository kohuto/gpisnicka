# Vytvoření Modelu pro Rozpoznávání Obrázků Zvířat (Kráva vs. Ovce)

V tomto tutoriálu se naučíš, jak vytvořit model, který dokáže rozpoznávat zvířata (kráva nebo ovce) z obrázků pomocí knihovny TensorFlow a Keras. Tutoriál tě provede celým procesem od přípravy dat až po trénink a testování modelu.

## Požadavky
Než začneme, ujisti se, že máš nainstalované potřebné knihovny:

1. **Python**: Ujisti se, že máš nainstalovanou aktuální verzi Pythonu.
2. **TensorFlow**: Tento framework budeme používat pro stavbu a trénink neuronových sítí.
3. **OpenCV**: Knihovna pro zpracování obrázků.
4. **NumPy**: Knihovna pro práci s poli a matematickými operacemi.

Instalace knihoven:
```bash
pip install tensorflow opencv-python numpy
```

---

## 1. Příprava obrázků
Vytvoř si složku, do které budeme celý projekt ukládat.
### a) Organizace složek
Nejprve potřebujeme připravit dataset (sadu obrázků), který bude obsahovat obrázky krav a ovcí. Vytvoř složku s názvem `dataset`. V této složce vytvoř další dvě složky:
- `cow/` pro obrázky krav
- `sheep/` pro obrázky ovcí

Struktura složek by měla vypadat takto:
```
dataset/
    cow/
        krava1.jpg
        krava2.jpg
        ...
    sheep/
        ovce1.jpg
        ovce2.jpg
        ...
```

---

## 2. Kód pro předzpracování a augmentaci obrázků

Náš model potřebuje obrázky v jednotné velikosti a dobře připravené pro trénink. To uděláme pomocí knihovny OpenCV a Keras.

### a) Nastavení konstant
Nejprve nastavíme několik konstant, které budou řídit velikost obrázků a velikost dávky (počet obrázků na jeden krok tréninku).

```python
import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Constants
IMG_SIZE = 128
BATCH_SIZE = 32
```

### b) Předzpracování obrázku
Vytvoříme funkci, která přijme obrázek, zmenší ho na 128x128 pixelů (tak, aby všechny obrázky měly stejnou velikost), a normalizuje jeho hodnoty (hodnoty pixelů se převedou z rozsahu 0-255 do rozsahu 0-1).

```python
def preprocess_image(image):
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    image = image / 255.0  # Normalize to [0, 1]
    return image
```

### c) Augmentace obrázků
Abychom modelu pomohli lépe se učit a nebyl omezen jen na konkrétní obrázky, použijeme augmentaci. To znamená, že náhodně otáčíme, posouváme a zvětšujeme obrázky během tréninku.

```python
# Image Data Generator for Augmentation
datagen = ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    validation_split=0.2  # Use 20% of images for validation
)
```

### d) Příprava trénovací a validační sady
Nyní použijeme `ImageDataGenerator` pro nahrání obrázků a vytvoření trénovací a validační sady. 80 % obrázků bude použito pro trénink a 20 % pro validaci.

```python
train_generator = datagen.flow_from_directory(
    'dataset/',
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='training'
)

validation_generator = datagen.flow_from_directory(
    'dataset/',
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='validation'
)
```

---

## 3. Vytvoření a Trénink Modelu

### a) Architektura modelu
Použijeme jednoduchou **Convolutional Neural Network (CNN)**, která se skládá z několika vrstev pro zpracování obrázků (sloje konvolučních vrstev a pooling vrstev), a nakonec přidáme plně propojené vrstvy pro rozhodování, zda se jedná o krávu nebo ovci.

```python
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])
```

### b) Kompilace modelu
Předtím, než začneme trénovat, musíme model zkompilovat. Použijeme Adam optimizer a binární křížovou entropii, protože jde o binární klasifikaci (kráva vs. ovce).

```python
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()
```

### c) Trénink modelu
Nyní můžeme začít trénovat model na našem datasetu.

```python
model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=10
)
```

### d) Vyhodnocení modelu
Po dokončení tréninku vyhodnotíme náš model na validační sadě.

```python
loss, accuracy = model.evaluate(validation_generator)
print(f'Validation accuracy: {accuracy*100:.2f}%')
```

---

## 4. Uložení modelu
Abychom model mohli použít později, uložíme ho do souboru.

```python
model.save('cow_sheep_classifier.h5')
```

---

## 5. Predikce nového obrázku

Nyní vytvoříme funkci, která přijme nový obrázek a předpoví, zda jde o krávu nebo ovci.

```python
def predict_image(image_path):
    image = cv2.imread(image_path)
    image = preprocess_image(image)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    prediction = model.predict(image)
    return 'cow' if prediction[0] < 0.5 else 'sheep'
```

Tuto funkci můžeme použít následovně:

```python
result = predict_image('/Users/ondrejkohut/Desktop/mojeprvniAI/dataset/new_images/whoknows1.jpeg')
print(result)
```

Pokud obrázek odpovídá krávě, výstup bude `cow`, pokud ovci, výstup bude `sheep`.

---

## 6. Závěr
Gratuluji! Dokončili jsme model, který dokáže rozpoznávat krávy a ovce z obrázků. Pomocí tohoto základního modelu můžeš pracovat s různými datasetami a vylepšovat svůj kód přidáním více tříd (např. dalších zvířat) nebo úpravou architektury modelu.


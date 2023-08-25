from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    material_category = {
        'oi': 'Oil Paint',
        'ac': 'Acrylic Paint',
        'wa': 'Watercolour Paint',
        'in': 'Ink Paint',
        'br': 'Brush',
        'pe': 'Pencil',
        'ca': 'Canvas',
        'pa': 'Paper',
    }

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class HarmfulMaterials(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    harm_category = {
        'le': 'Lead',
        'ca': 'Cadmium',
        'me': 'Mercury',
        'so': 'Solvents',
        'mm': 'Methyl Methacrylate',
        'ar': 'Aromatic Hydrocarbons'
    }

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Material(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    harmful_content = models.CharField(
        max_length=2,  
        choices=[(key, value) for key, value in HarmfulMaterials.harm_category.items()],
        null=True, blank=True
    )
    material_category = models.CharField(
        max_length=2,  
        choices=[(key, value) for key, value in Category.material_category.items()],
        null=True, blank=True
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    type = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    online_exclusive = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
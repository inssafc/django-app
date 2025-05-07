from django.core.management.base import BaseCommand
from django.core.files import File
from store.models import Category, Product
import os

class Command(BaseCommand):
    help = 'Crée une catégorie de sacs à dos et 10 produits'

    def handle(self, *args, **kwargs):
        # Créer la catégorie si elle n'existe pas
        category, created = Category.objects.get_or_create(
            name='Sacs à dos',
            defaults={'description': 'Sacs à dos pour diverses activités'}
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Catégorie "Sacs à dos" créée avec succès'))
        
        # Définir les informations des sacs à dos
        backpacks = [
            {
                'name': 'Sac à dos de randonnée Pro',
                'description': 'Parfait pour les longues randonnées avec de nombreux compartiments.',
                'price': 89.99,
                'stock': 25
            },
            {
                'name': 'Sac à dos étudiant Classic',
                'description': 'Idéal pour les étudiants, avec compartiment pour ordinateur portable.',
                'price': 49.99,
                'stock': 50
            },
            {
                'name': 'Sac à dos tactique militaire',
                'description': 'Robuste et résistant, pour les conditions extrêmes.',
                'price': 129.99,
                'stock': 15
            },
            {
                'name': 'Sac à dos de voyage Weekend',
                'description': 'Parfait pour les escapades de weekend.',
                'price': 79.99,
                'stock': 30
            },
            {
                'name': 'Sac à dos sportif Athlete',
                'description': 'Léger et pratique pour le sport et les activités de plein air.',
                'price': 59.99,
                'stock': 40
            },
            {
                'name': 'Sac à dos urbain City',
                'description': 'Élégant et pratique pour la vie urbaine.',
                'price': 69.99,
                'stock': 35
            },
            {
                'name': 'Sac à dos anti-vol Secure',
                'description': 'Avec des caractéristiques anti-vol pour protéger vos biens.',
                'price': 99.99,
                'stock': 20
            },
            {
                'name': 'Sac à dos pour appareil photo',
                'description': 'Spécialement conçu pour les photographes.',
                'price': 109.99,
                'stock': 18
            },
            {
                'name': 'Sac à dos imperméable Aqua',
                'description': '100% imperméable pour protéger vos affaires par tous les temps.',
                'price': 84.99,
                'stock': 22
            },
            {
                'name': 'Sac à dos enfant Junior',
                'description': 'Coloré et pratique pour l\'école.',
                'price': 39.99,
                'stock': 45
            }
        ]
        
        # Créer les produits
        products_created = 0
        for backpack in backpacks:
            product, created = Product.objects.get_or_create(
                name=backpack['name'],
                defaults={
                    'description': backpack['description'],
                    'price': backpack['price'],
                    'stock': backpack['stock'],
                    'category': category
                }
            )
            
            if created:
                products_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'{products_created} sacs à dos créés avec succès'))
from django.db import models
from django_jsonform.models.fields import JSONField

# Create your models here.
class FormConfig(models.Model):
    form_schema = {
		'type': 'array',
		'items': {
			'type': 'object',
			'properties': {
				'option': {
					'type': 'object',
					'properties': {
						'name': {
							'type': 'string'
						},
						'option_type': {
							'oneOf': [
								{
									'type': 'string',
									'title': 'String',
									'widget': 'hidden'
								},
								{
									'type': 'number',
									'title': 'Number',
									'widget': 'hidden',
								},
								{
									'type': 'object',
									'title': 'List',
									'properties': {
										'type': {
											'type': 'string',
											'default': 'list',
											'widget': 'hidden'
										},
										'list_name': {
											'type': 'string',
											'choices': [
												'emails',
												'keywords'
											]
										}
									}
								}
							]
						}
					}
				}
			}
		}
	}
    name = models.CharField(max_length=100)
    options = JSONField(schema=form_schema)




class ShoppingList(models.Model):
    ITEMS_SCHEMA = {
        'type': 'array', # a list which will contain the items
        'items': {
            'type': 'string' # items in the array are strings
        }
    }

    items = JSONField(schema=ITEMS_SCHEMA)
    date_created = models.DateTimeField(auto_now_add=True)
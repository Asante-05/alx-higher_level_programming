#include "header.h"
/**
 * hash_table_create - function to create a hash table of size (size)
 * @size: defines the size of the table
 * Return: a pointer to the newly created table
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *table = (hash_table_t *)malloc(sizeof(hash_table_t);

	table->size = size;

	for (int i = 0; i < table->size; i++)
	{
		table->array[i] = NULL;
	}

	return (table);
}

#include "lists.h"
/**
 * insert_node - functiont to insert node
 * @head: double pointer to head node
 * @number: number to be inserted
 * Return: (pointer to node) on Success else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *new;

	temp = *head;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
	{
		free(new);
		return (NULL);
	}

	if (*head == NULL || number < (*head)->n)
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}

	while (temp->next->n < number)
	{
		temp = temp->next;
	}

	new->next = temp->next;
	new->n = number;
	temp->next = new;
	return (new);
}

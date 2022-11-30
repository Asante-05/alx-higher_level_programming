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
		free(new);
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	else
	{
			while (temp->next->n < number)
			{
				temp = temp->next;
			}
	}

	new->next = temp->next;
	temp->next = new;
	return (new);
}

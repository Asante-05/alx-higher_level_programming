#include "lists.h"
/**
 * check_cycles - function to check if a linked is cyclic
 * @list: pointer to head of linked list
 * Return: 1 if linked is cylcic else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *tail;

	if (list == NULL)
		return (0);

	head = list;
	tail = list;

	while(tail != NULL && tail->next != NULL)
	{
		head = head->next;
		tail = tail->next->next;

		if (head == tail)
			return (1);
	}
}

#include "lists.h"
/**
 * check_cycles - function to check if a linked is cyclic
 * @list: pointer to head of linked list
 * Return: 1 if linked is cylcic else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	int n = 0;

	head = list;
	while (list != NULL)
	{
		list = list->next;
		if (head == list)
			n = 1;
	}
	return (n);
}

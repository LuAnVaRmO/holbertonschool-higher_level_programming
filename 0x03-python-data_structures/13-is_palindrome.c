#include "lists.h"
/**
 * is_palindrome - Function that checks if a singly linked list is a palindrome
 * @head: pointer to the first element of a linked list
 * Return: 1 if the list is palindrome or 0 if is not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *cmp = (*head);
	int temp[1024];
	int i = 0, j;

	if (head == NULL || *head == NULL)
		return (1);
	while (cmp)
	{
		temp[i] = cmp->n;
		cmp = cmp->next;
		i++;
	}
	i = i - 1;
	for (j = 0; j <= i ; j++)
	{
		if (temp[i] != temp[j])
			return (0);
		 i--;
	}
	return (1);
}

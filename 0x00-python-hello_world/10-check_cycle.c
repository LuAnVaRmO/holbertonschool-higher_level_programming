#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Check a linked list
 * @list: the linked list
 * Description: Check if a linked list is a cycle or not
 * Return: 0 if no, 1 if cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *first = list;
    listint_t *last = list;
    if (last != NULL)
    {
        while(first != NULL && first->next != NULL)
        {
            last = last->next;
            first = first->next;
            first = first->next;
            if(first == last)
                return(1);
        }
    }
    return(0);
}


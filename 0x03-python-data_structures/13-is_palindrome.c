#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head);

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to the head of the linked list
 *
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head);

/**
 * compare_lists - compares two linked lists
 * @list1: pointer to the first linked list
 * @list2: pointer to the second linked list
 *
 * Return: 1 if lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2);

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev_slow = NULL;
    listint_t *second_half, *mid_node = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (is_palindrome);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        mid_node = slow;
        slow = slow->next;
    }

    second_half = reverse_list(&slow);

    is_palindrome = compare_lists(*head, second_half);

    second_half = reverse_list(&second_half);

    if (mid_node != NULL)
    {
        prev_slow->next = mid_node;
        mid_node->next = second_half;
    }
    else
    {
        prev_slow->next = second_half;
    }

    return (is_palindrome);
}

listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return (*head);
}

int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return (0);

        list1 = list1->next;
        list2 = list2->next;
    }

    return (1);
}


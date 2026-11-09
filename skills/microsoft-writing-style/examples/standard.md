# Clearing a Windows clipboard without losing two keepers

[한국어](standard.ko.md) · [light](light.md) · **standard** · [strict](strict.md)

### Question

> My Windows 11 clipboard history has five entries. A delivery address and an obsolete access code are pinned. A return reference and two draft notes are unpinned. I want to keep just the address and the return reference without typing either again. The interface is in English: Windows logo key + V opens Clipboard history, Pin protects an entry from Clear all, Clear all removes unpinned entries, and See more (...) > Delete removes one entry. How can I use Clear all on this PC and still end up with exactly those two items?

**Sources** · [Microsoft Support, Using the clipboard](https://support.microsoft.com/en-us/windows/apps/using-the-clipboard) · To keep the return reference, pin it before choosing **Clear all**.

### With the skill

> Open Clipboard history with Windows logo key + V, then set up the entries:
>
> | Entry | Current state | Keep or remove | Action to take now |
> |---|---|---|---|
> | Delivery address | Pinned | Keep | Leave it pinned |
> | Obsolete access code | Pinned | Remove | Select See more (...) > Delete |
> | Return reference | Unpinned | Keep | Select Pin |
> | Draft note 1 | Unpinned | Remove | Leave it unpinned |
> | Draft note 2 | Unpinned | Remove | Leave it unpinned |
>
> After those steps, select **Clear all**. Check Clipboard history: it should contain only the delivery address and return reference.

### Without the skill

> In Clipboard history, delete the obsolete access code first:
>
> 1. Press **Windows logo key + V**.
> 2. Find the access code, select **See more (…) > Delete**.
> 3. Select **Clear all**.
>
> The pinned address stays protected, and Clear all removes the unpinned return reference and both draft notes. To keep the return reference without retyping it, copy it again from its original source and pin the new clipboard entry. You’ll then have exactly the address and return reference.

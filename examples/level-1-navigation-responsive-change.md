# Level 1: CHECKPOINT Navigation Responsive Change

## Request

Tighten spacing in `MobileNav`.

## Before

```tsx
export function MobileNav({ links, isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <nav aria-label="Mobile navigation" className="fixed inset-x-0 top-0 p-6">
      <button type="button" onClick={onClose}>Close</button>
      <ul className="space-y-4">
        {links.map((link) => (
          <li key={link.href}>
            <a href={link.href}>{link.label}</a>
          </li>
        ))}
      </ul>
    </nav>
  );
}
```

## After

```tsx
export function MobileNav({ links, isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <nav aria-label="Mobile navigation" className="fixed inset-x-0 top-0 p-4">
      <button type="button" onClick={onClose}>Close</button>
      <ul className="space-y-3">
        {links.map((link) => (
          <li key={link.href}>
            <a href={link.href}>{link.label}</a>
          </li>
        ))}
      </ul>
    </nav>
  );
}
```

## Expected Skill Output

```text
UI Invariant Checkpoint
Risk Gate: CHECKPOINT because this changes responsive navigation layout around preserved interaction and semantics.

Preserve:
- Closed branch remains present. Evidence: INSPECTED.
- Close button remains type="button" and calls onClose. Evidence: INSPECTED.
- nav keeps aria-label="Mobile navigation". Evidence: INSPECTED.

Permit:
- Tighten nav and list spacing.

Probe:
- 390px mobile viewport not checked.

Evidence:
- Checked: none.
- Inspected: diff, close button, nav label, link mapping.
- Not checked: browser rendering, keyboard path, mobile viewport.

Post-diff Risk Recheck:
- Initial mode: CHECKPOINT
- Actual touched concerns: responsive fixed nav layout
- Final mode: CHECKPOINT
- Reason: interaction and semantic attributes were inspected and preserved.
```

## Why This Is CHECKPOINT

The diff is visual, but it touches a fixed responsive navigation surface. It preserves handlers and semantics but still needs viewport review.

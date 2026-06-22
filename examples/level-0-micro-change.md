# Level 0: MICRO Change

## Request

Increase the padding in `PricingCard`.

## Before

```tsx
export function PricingCard({ plan, price }) {
  return (
    <section className="rounded border p-4">
      <h2>{plan}</h2>
      <p>{price}</p>
    </section>
  );
}
```

## After

```tsx
export function PricingCard({ plan, price }) {
  return (
    <section className="rounded border p-6">
      <h2>{plan}</h2>
      <p>{price}</p>
    </section>
  );
}
```

## Expected Skill Output

```text
Micro-check:
- Scope: spacing-only class change in PricingCard.
- Behavior touched: no conditionals, handlers, data flow, roles, labels, or accessibility attributes changed.
- Verification: diff inspected.
```

## Static Check

```text
PASS no behavior-looking token changed
```

## Why This Is MICRO

The diff changes only a static spacing class. It does not touch conditional rendering, state, handlers, form behavior, accessibility semantics, data mapping, routing, responsive guards, or public props.

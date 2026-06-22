# Level 1: CHECKPOINT Change

## Request

Clean up the layout of `ProductSummary`.

## Before

```tsx
export function ProductSummary({ product, isLoading, error }) {
  if (isLoading) {
    return <div role="status">Loading product...</div>;
  }

  if (error) {
    return <p role="alert">{error.message}</p>;
  }

  return (
    <article className="space-y-3">
      <h2>{product.name}</h2>
      <p>{product.description}</p>
      <a href={`/products/${product.id}`}>View details</a>
    </article>
  );
}
```

## After

```tsx
export function ProductSummary({ product, isLoading, error }) {
  if (isLoading) {
    return <div role="status">Loading product...</div>;
  }

  if (error) {
    return <p role="alert">{error.message}</p>;
  }

  return (
    <article className="grid gap-4 rounded border p-4">
      <div className="grid gap-1">
        <h2>{product.name}</h2>
        <p>{product.description}</p>
      </div>
      <a href={`/products/${product.id}`}>View details</a>
    </article>
  );
}
```

## Expected Skill Output

```text
UI Invariant Checkpoint
Risk Gate: CHECKPOINT because this is a local layout cleanup with loading and error branches nearby.

Preserve:
- Loading branch with role="status" remains present. Evidence: INSPECTED.
- Error branch with role="alert" remains present. Evidence: INSPECTED.
- Product details link still points to /products/${product.id}. Evidence: INSPECTED.

Permit:
- Rework article spacing and grouping.

Probe:
- Responsive layout not checked in browser.

Evidence:
- Checked: none.
- Inspected: diff, loading branch, error branch, details link.
- Not checked: browser rendering or viewport behavior.

Post-diff Risk Recheck:
- Initial mode: CHECKPOINT
- Actual touched concerns: local layout around preserved conditional branches
- Final mode: CHECKPOINT
- Reason: no state, handler, data mapping, or accessibility behavior was edited.
```

## Static Checks

```text
PASS preserved if (isLoading)
PASS preserved role="status"
PASS preserved if (error)
PASS preserved role="alert"
PASS preserved href={`/products/${product.id}`}
```

## Why This Is CHECKPOINT

The request sounds visual, but the component contains loading and error branches. The branches were inspected and preserved, while browser and viewport behavior remain unverified.

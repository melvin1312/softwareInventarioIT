---
name: Corporate Modernist
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#45464d'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#0051d5'
  on-secondary: '#ffffff'
  secondary-container: '#316bf3'
  on-secondary-container: '#fefcff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#191c1e'
  on-tertiary-container: '#818486'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#dbe1ff'
  secondary-fixed-dim: '#b4c5ff'
  on-secondary-fixed: '#00174b'
  on-secondary-fixed-variant: '#003ea8'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '600'
    lineHeight: 38px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  mono-md:
    fontFamily: monospace
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-margin: 32px
  gutter: 24px
  card-padding: 20px
  table-cell-padding: 12px 16px
---

## Brand & Style

This design system is built upon the pillars of reliability, transparency, and operational efficiency. Designed for IT professionals managing complex infrastructures, the aesthetic avoids visual clutter in favor of high-density data clarity. 

The style is **Corporate / Modern**, characterized by a disciplined use of whitespace, a structured hierarchy, and subtle interactive cues. It evokes the feeling of a precision instrument—high-end, dependable, and authoritative. Every element exists to facilitate the quick identification of assets and their current lifecycle status.

## Colors

The palette is rooted in deep slate and sapphire tones to establish a foundation of stability. 

- **Primary:** A deep Slate-900 used for core branding, primary navigation backgrounds, and high-level headings.
- **Secondary:** A vibrant Blue-600 serves as the action color, guiding the eye toward primary buttons and active states.
- **Tertiary/Surface:** Ultra-light grays (F8FAFC) provide subtle containment for data tables and dashboard cards without introducing heavy visual weight.
- **Semantic Palette:** Specific shades are reserved for asset status: Emerald for availability, Blue for assignments, and Amber for maintenance.

## Typography

This design system utilizes **Inter** exclusively to leverage its exceptional readability at small sizes and high-density screens. 

Tight letter spacing is applied to headings to maintain a modern, "compact" feel. Body text uses standard tracking to ensure long lists of asset serial numbers and specifications remain legible. A monospace fallback is specifically designated for hardware IDs and IP addresses to ensure character distinction (e.g., distinguishing '0' from 'O').

## Layout & Spacing

The layout follows a **fixed-fluid hybrid grid**. The side navigation is fixed at 280px, while the main content area utilizes a 12-column fluid grid system. 

The spacing rhythm is based on a 4px baseline, but defaults to a 20px (5x) standard for internal component padding to allow for a "breathable" feel within dense data environments. Data tables utilize a condensed vertical rhythm (12px) to maximize the amount of information visible above the fold.

## Elevation & Depth

This design system uses **Tonal Layers** supplemented by **Low-contrast Outlines** rather than heavy shadows. This keeps the interface feeling "flat" and performant.

- **Level 0 (Base):** Background color (Slate-50).
- **Level 1 (Cards):** White background with a 1px border (Slate-200). No shadow.
- **Level 2 (Dropdowns/Modals):** White background, 1px border, and a soft, highly diffused 12% opacity shadow (Slate-900/10) to suggest separation from the work surface.
- **Interactive Depth:** Buttons use a subtle 1px inset bottom border to provide a tactile "pressed" feel without skeuomorphism.

## Shapes

The system utilizes a **Soft (0.25rem)** corner radius. This choice balances the professional rigidity of a "sharp" corporate tool with the modern approachability of SaaS. 

Status badges and tags use a slightly more aggressive radius (rounded-lg) to distinguish them from structural elements like input fields and containers. Action buttons maintain the standard 4px radius to align with the grid's precision.

## Components

### Data Tables
Tables are the core of the system. Use a clean header with a subtle Slate-100 background. Row hover states should use a very faint Blue-50 to indicate selection. Use "zebra striping" only if tables exceed 20 columns.

### Status Badges
Badges use a "soft-pill" style: a light tinted background with a high-contrast text color of the same hue (e.g., Available: Emerald-100 background with Emerald-700 text).

### Search & Filter Bar
The global search bar should be prominent, featuring a 1px Slate-300 border and a leading magnifying glass icon. Filter "pills" should appear below the search bar to show active constraints.

### Action Buttons
- **Primary:** Solid Blue-600 with white text. 
- **Secondary:** White background with Slate-300 border and Slate-700 text.
- **Ghost:** No border, Blue-600 text, used for "Cancel" or "Clear" actions.

### Asset Cards
For gallery views, cards must include a small thumbnail of the hardware category icon in the top-right and a clear bold title for the Asset Tag ID.
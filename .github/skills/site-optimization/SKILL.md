---
name: site-optimization
description: "Use when: updating a marketing landing page, adding lead-generation widgets, patching HTML/CSS/JS for conversion improvements, or validating a static website before launch."
---

# Site Optimization Workflow

## Purpose

Use this skill to improve a marketing or lead-generation website by turning static page content into a higher-converting, more polished user experience. The workflow is designed for landing pages that need calls to action, lead capture, content modules, SEO metadata, and lightweight interactive behavior without a full framework or CMS.

## Core Workflow

### 1. Identify the conversion goal
Before editing, define the target outcome.
- Is the goal to collect leads, drive calls, surface a free resource, or increase page engagement?
- Which sections are most important: hero, services, knowledge center, contact form, footer, or trust elements?
- Which page should be modified: home page, article page, FAQ page, or a shared template?

If the site has multiple conversion points, prioritize the highest-value path first.

### 2. Inspect the existing structure
Read the relevant page and supporting assets before changing anything.
- Review the existing HTML for section structure, IDs, form elements, and anchor targets.
- Check CSS for styling conventions, spacing, and reusable utility patterns.
- Review JavaScript for existing interactions, event listeners, and DOM initialization.

Decision point:
- If a feature already exists in another page, reuse its pattern instead of reinventing it.
- If the page uses a static layout, make the change with minimal disruption to the existing design system.

### 3. Add the user-facing improvement
Implement only the feature needed for the current objective.

Examples include:
- Add a CTA button to the hero area
- Add a modal for a free resource or lead magnet
- Insert a subscription form into a knowledge section
- Add a service-link or anchor for related guidance
- Add structured SEO tags for better search visibility
- Update contact form configuration for a real endpoint

Good practice:
- Prefer targeted HTML insertion in the correct section rather than broad rewrites.
- Reuse existing class names and layout conventions so the page remains coherent.
- Keep IDs and selectors consistent with the current JavaScript and CSS.

### 4. Patch the supporting CSS and JS
When the new UI requires interactivity or a custom style, add the smallest possible updates.
- Append CSS rules near related sections instead of rewriting the entire stylesheet.
- Add JavaScript only for event handlers or interactions directly tied to the new feature.
- Guard against missing DOM elements with safe checks such as optional chaining when necessary.

Decision point:
- If the feature is purely decorative, CSS may be enough.
- If it opens/closes a dialog, submits a form, or triggers behavior, add the corresponding JS.

### 5. Validate the result in a browser
Once the changes are written, confirm the page behaves correctly.
- Load the page locally in a browser.
- Check that CTAs render properly and are visible in the correct sections.
- Verify modal open/close behavior, form markup, and anchor navigation.
- Ensure page styling remains consistent across the original layout.
- Check that there are no broken links, empty IDs, or missing assets.

Completion criteria:
- The change works from a user point of view.
- The generated page remains visually coherent and readable.
- The feature matches the intended conversion objective without introducing regressions.

## Quality Standards

A change is done when all of the following are true:
- The page remains functional and readable.
- The added element aligns with the brand and layout.
- The conversion element is visible where users expect it.
- Forms, buttons, anchors, and modals work without console-breaking errors.
- The styling is concise and not overly invasive to the design system.
- The implementation is maintainable and easy to adjust later.

## Branching Logic

### If the request is content-only
- Update the HTML text, section headings, or CTAs.
- Keep styling changes minimal unless the text breaks the layout.

### If the request includes interactivity
- Add a modal, form handler, or event-driven behavior.
- Add the corresponding CSS and JS only for the exact interaction.

### If the request includes SEO or trust-building enhancements
- Add metadata, schema markup, canonical links, and business information.
- Check that placeholder values are clearly marked for replacement before production deployment.

### If the request involves form submission
- Confirm the endpoint or service target is configured.
- If the endpoint is placeholder data, flag it as a final deployment step rather than silently leaving it embedded.

## Recommended Prompt Pattern

Use prompts such as:
- “Improve this landing page by adding a lead magnet modal and matching CTA buttons.”
- “Add a knowledge subscription block and make the footer contact link open the same resource modal.”
- “Patch this static HTML/CSS/JS site to include a contact form and SEO metadata without breaking the layout.”
- “Audit this marketing page for conversion improvements and implement the top-priority changes.”

## Example Execution Checklist

1. Read the relevant HTML, CSS, and JS.
2. Identify the key user action and the best insertion point.
3. Add the new content or elements.
4. Add the necessary CSS and JS for behavior.
5. Verify the page in a browser.
6. Check for broken selectors, missing IDs, and placeholder deployment values.
7. Finalize with a clean, production-ready result.

## Notes for Reuse

This skill is most effective for static sites, brochure-style corporate pages, lead-generation landing pages, and small marketing websites where the solution should stay lightweight, editable, and fast to deploy.

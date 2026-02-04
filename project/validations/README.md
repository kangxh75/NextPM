# Validations

This folder contains **validation documentation for completed features**.

## Purpose

Document that features work as specified. Proof that:
- ✅ Implementation matches spec
- ✅ Acceptance criteria are met
- ✅ Tests pass (manual or automated)
- ✅ Edge cases are handled

## When to Create Validation Docs

After completing tasks for a feature:
1. Test the implementation
2. Document test results
3. Note any deviations from spec
4. Record lessons learned

## Validation Template

```markdown
# [Feature Name] - Validation

**Spec:** Link to `/specs/[feature-name].md`
**Tasks:** Link to `/tasks/[feature-name]-tasks.md`
**Date:** YYYY-MM-DD

## Summary

✅ / ⚠️ / ❌ Overall status

Brief summary of validation outcome.

## Test Results

### Test 1: [Test Name]
**Expected:** What should happen
**Actual:** What happened
**Status:** ✅ Pass / ❌ Fail

### Test 2: [Test Name]
...

## Acceptance Criteria

From the original spec:
- [x] Criterion 1 - Met
- [x] Criterion 2 - Met
- [ ] Criterion 3 - Not met (reason)

## Known Issues

List any bugs, limitations, or deviations:
- Issue 1
- Issue 2

## Manual Testing Steps

Document how to manually test this feature:
1. Step 1
2. Step 2
3. Expected result

## Automated Tests

If applicable:
- Test file: `tests/test_feature.py`
- Coverage: X%
- All tests passing: ✅

## Performance

If relevant:
- Load time: X ms
- Response time: X ms
- Memory usage: X MB

## Lessons Learned

**What Went Well:**
- Thing 1
- Thing 2

**What Could Be Better:**
- Thing 1
- Thing 2

**AI Assistance:**
- What AI tools were helpful?
- What prompts worked well?
- Time saved estimate

## Next Steps

- [ ] Follow-up task 1
- [ ] Follow-up task 2

---

**Sign-off:** Ready to merge / Needs fixes / Blocked
```

## Types of Validation

**Manual Testing:**
- Click through UI
- Test different scenarios
- Verify against spec

**Automated Testing:**
- Unit tests
- Integration tests
- Test coverage reports

**Code Review:**
- AI-assisted code review
- Self-review against spec
- Check conventions

**User Testing:**
- Internal dogfooding
- Beta user feedback

## Naming Convention

Match the related spec and tasks:
- Spec: `dark-mode-feature.md`
- Tasks: `dark-mode-tasks.md`
- Validation: `dark-mode-validation.md`

## Using AI for Validation

AI can help with:
- **Test case generation**: "Generate test cases for this spec"
- **Test execution**: AI coding assistants can write and run tests
- **Documentation**: "Summarize these test results"

---

**Tip**: Validation isn't just about finding bugs—it's about building confidence that your implementation matches your intent.

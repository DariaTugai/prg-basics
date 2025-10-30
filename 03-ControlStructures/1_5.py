total_tasks = 20
tasks_ok = 10
your_total_tasks = int(input('Enter number of tasks completed successfully: '))
test_passed = False

if your_total_tasks >= tasks_ok:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')
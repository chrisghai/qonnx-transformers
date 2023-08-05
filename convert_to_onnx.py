from argparse import ArgumentParser
from optimum.exporters.onnx import main_export
from optimum.exporters.tasks import TasksManager

VALID_TASKS = list(TasksManager._TASKS_TO_LIBRARY.keys())


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-m", "--model", dest="model", required=True)
    parser.add_argument("-t", "--task", dest="task", default="")

    args = parser.parse_args()
    task = args.task
    if not task or task not in VALID_TASKS:
        print(f"{task} is not valid! It must be one of: {VALID_TASKS}")
        exit(1)

    model = args.model
    main_export(args.model, 
                output=f"{model}-onnx", 
                task=task)
    print("Model converted to ONNX format!")
    
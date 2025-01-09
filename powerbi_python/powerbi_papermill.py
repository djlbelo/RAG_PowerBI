import papermill as pm
import nbformat


def execute_notebook_with_papermill(input_path, output_path, parameters=None):
    """
    Execute a Jupyter notebook using papermill.

    Args:
        input_path (str): Path to the input notebook.
        output_path (str): Path to save the executed notebook.
        parameters (dict, optional): Parameters to inject into the notebook.
    """
    try:
        print("Starting notebook execution with papermill...")

        # Inject parameters if provided
        if parameters is None:
            parameters = {}

        # Execute the notebook with papermill
        pm.execute_notebook(
            input_path=input_path,
            output_path=output_path,
            parameters=parameters
        )

        print(f"Notebook executed successfully and saved to {output_path}")

    except Exception as e:
        print(f"Error during notebook execution: {e}")


if __name__ == "__main__":
    # Replace these with your notebook paths
    input_notebook = "notebook_copy.ipynb"
    output_notebook = "executed_notebook1.ipynb"

    execute_notebook_with_papermill(input_notebook, output_notebook)

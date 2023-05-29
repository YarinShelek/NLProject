from sklearn.metrics import classification_report


def evaluate_model(y_true, y_pred):
    report = classification_report(y_true, y_pred, digits=4)
    print(report)

    class_report = classification_report(y_true, y_pred, output_dict=True)

    precision_off = class_report["1"]['precision']
    recall_off = class_report["1"]['recall']
    f1_off = class_report["1"]['f1-score']

    precision_not = class_report["0"]['precision']
    recall_not = class_report["0"]['recall']
    f1_not = class_report["0"]['f1-score']

    print(f"OFF Precision: {precision_off:.4f}")
    print(f"OFF Recall: {recall_off:.4f}")
    print(f"OFF F1-Score: {f1_off:.4f}")

    print(f"Not Precision: {precision_not:.4f}")
    print(f"Not Recall: {recall_not:.4f}")
    print(f"Not F1-Score: {f1_not:.4f}")
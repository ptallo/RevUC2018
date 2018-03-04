import tensorflow as tf


class tensorFlowAPIObject:
    def __init__(self, dataSet):
        self.featureColumns = []
        for key in dataSet.keys():
            featureColumn = tf.feature_column.numeric_column(key=key)
            self.featureColumns.append(featureColumn)
        self.model = tf.estimator.DNNClassifier(
            feature_columns=self.featureColumns,
            hidden_units=[10, 10],
            n_classes=7
        )

    def trainInputFn(self, features, labels, batch_size):
        dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
        dataset = dataset.shuffle(buffer_size=1000).repeat(count=None).batch(batch_size)
        return dataset.make_one_shot_iterator().get_next()

    def train(self, trainDataSet, trainDataSetLabels, batchSize, trainSteps):
        self.model.train(
            input_fn=lambda:self.trainInputFn(trainDataSet, trainDataSetLabels, batchSize),
            steps=trainSteps
        )

    def evalInputFn(self, features, labels=None, batchSize=1000):
        """An input function for evaluation or prediction"""
        if labels is None:
            # No labels, use only features.
            inputs = features
        else:
            inputs = (features, labels)

        # Convert inputs to a tf.dataset object.
        dataset = tf.data.Dataset.from_tensor_slices(inputs)

        # Batch the examples
        assert batchSize is not None, "batch_size must not be None"
        dataset = dataset.batch(batchSize)

        # Return the read end of the pipeline.
        return dataset.make_one_shot_iterator().get_next()

    def eval(self, features, labels, batchSize):
        eval_result = self.model.evaluate(
            input_fn=lambda: self.evalInputFn(features, labels, batchSize)
        )
        print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    def predict(self, features, batchSize):
        predictions = self.model.predict(
            input_fn=lambda: self.evalInputFn(features, batchSize)
        )
        return predictions
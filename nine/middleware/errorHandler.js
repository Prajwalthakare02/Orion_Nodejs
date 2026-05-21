const errorHandler = (err, req, res, next) => {
  const statusCode = err.statusCode || 500;
  const status = err.status || (statusCode >= 500 ? 'error' : 'fail');
  const response = {
    status,
    message: statusCode >= 500 ? 'Internal Server Error' : err.message
  };

  if (err.errors) {
    response.errors = err.errors;
  }

  if (err.isOperational === false || statusCode >= 500) {
    console.error(err);
  }

  res.status(statusCode).json(response);
};

export default errorHandler;
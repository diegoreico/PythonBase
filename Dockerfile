# Build image
FROM python:3.10-slim
RUN pip install "poetry"

RUN mkdir /app
WORKDIR /app
ADD mymodule ./mymodule

ADD setup.py .
ADD pyproject.toml .

RUN set -ex && \
    poetry install --no-root &&\
    poetry build

     
# Final image
FROM python:3.10-slim

RUN mkdir /app
WORKDIR /app
COPY --from=0 /app/dist/mymodule-0.1.0-py3-none-any.whl ./
RUN pip install ./mymodule-0.1.0-py3-none-any.whl
# this is the entrypoint that is set inside the setup.py file
ENTRYPOINT ["mymodule"]

#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z postgres 5432; do
  sleep 0.5
done

echo "PostgreSQL started"
exec "$@"

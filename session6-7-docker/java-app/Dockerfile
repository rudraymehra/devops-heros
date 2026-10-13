FROM eclipse-temurin:21-jdk-alpine AS builder
WORKDIR /src
COPY Main.java .
RUN javac --add-modules jdk.httpserver Main.java

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=builder /src/Main.class .
USER 10001:10001
EXPOSE 8080
ENTRYPOINT ["java", "--add-modules", "jdk.httpserver", "Main"]

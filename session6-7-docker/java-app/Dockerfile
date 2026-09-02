# Java Hello World - multi-stage build
# Stage 1: compile with the full JDK
# (eclipse-temurin:17-jdk-alpine is amd64-only, so the multi-arch Ubuntu based tag is used
#  here to make the build work on Apple Silicon as well as on x86 Linux servers)
FROM eclipse-temurin:17-jdk AS build
WORKDIR /app
COPY Main.java .
RUN javac Main.java

# Stage 2: run with only the JRE (smaller image, no compiler shipped to production)
FROM eclipse-temurin:17-jre
WORKDIR /app
COPY --from=build /app/Main.class .

EXPOSE 8080

CMD ["java", "Main"]

import asyncio
import time
import aiohttp

# Configuración del test
URL = "http://localhost:8081/api/users/list"  # Reemplaza con tu URL local
CONCURRENCY = 10  # Número de peticiones simultáneas en paralelo
DURATION_SECONDS = 10  # Tiempo total de la prueba


async def fetch(session, url, stats):
    start_time = time.perf_counter()
    try:
        async with session.get(url) as response:
            await response.read()
            latency = time.perf_counter() - start_time
            stats["latencies"].append(latency)
            if response.status == 200:
                stats["success"] += 1
            else:
                stats["errors"] += 1
    except Exception:
        stats["errors"] += 1


async def worker(session, url, end_time, stats):
    while time.perf_counter() < end_time:
        await fetch(session, url, stats)


async def run_benchmark():
    stats = {"success": 0, "errors": 0, "latencies": []}

    print(f"🚀 Iniciando test contra {URL}")
    print(
        f"⏱️  Duración: {DURATION_SECONDS}s | Concurrencia (Workers): {CONCURRENCY}\n"
    )

    async with aiohttp.ClientSession() as session:
        end_time = time.perf_counter() + DURATION_SECONDS
        # Lanza workers concurrentes en paralelo
        tasks = [
            worker(session, URL, end_time, stats) for _ in range(CONCURRENCY)
        ]
        await asyncio.gather(*tasks)

    total_requests = stats["success"] + stats["errors"]
    latencies = stats["latencies"]

    # Mostrar métricas obtenidas
    print("=== RESULTADOS ===")
    print(f"Peticiones totales:  {total_requests}")
    print(f"Peticiones 200 OK:   {stats['success']}")
    print(f"Errores / Fallos:    {stats['errors']}")
    print(f"RPS (Req/segundo):   {total_requests / DURATION_SECONDS:.2f}")

    if latencies:
        avg_lat = (sum(latencies) / len(latencies)) * 1000
        min_lat = min(latencies) * 1000
        max_lat = max(latencies) * 1000
        print(f"Latencia promedio:  {avg_lat:.2f} ms")
        print(f"Latencia mínima:    {min_lat:.2f} ms")
        print(f"Latencia máxima:    {max_lat:.2f} ms")


if __name__ == "__main__":
    asyncio.run(run_benchmark())